# Copyright 2014 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""ELF parsing related helper functions/classes."""

import io
import os
import struct
from typing import Any, Dict, List, Optional, Set, Tuple, Union

from chromite.third_party import lddtree
from chromite.third_party.pyelftools.elftools.common import exceptions
from chromite.third_party.pyelftools.elftools.common import utils
from chromite.third_party.pyelftools.elftools.elf import elffile


def GetSymbolTableSize(elf: elffile.ELFFile) -> int:
    """Get Symbol Table size by parsing section header."""
    for i in range(elf["e_shnum"]):
        section = elf.get_section(i)  # type: ignore[no-untyped-call]
        if section["sh_type"] == "SHT_DYNSYM":
            return int(section["sh_size"])
    return 0


def ParseELFSymbols(elf: elffile.ELFFile) -> Tuple[Set[bytes], Set[bytes]]:
    """Parses list of symbols in an ELF file.

    Args:
        elf: The ELF file to parse.

    Returns:
        A 2-tuple of (imported, exported) symbols, each of which is a set.
    """
    imp: Set[bytes] = set()
    exp: Set[bytes] = set()

    if elf.header.e_type not in ("ET_DYN", "ET_EXEC"):
        return imp, exp

    for segment in elf.iter_segments():  # type: ignore[no-untyped-call]
        if segment.header.p_type != "PT_DYNAMIC":
            continue

        # Find strtab and symtab virtual addresses.
        symtab_ptr = None
        dthash_ptr = None
        symbol_size = (
            elf.structs.Elf_Sym.sizeof()  # type: ignore[no-untyped-call]
        )
        for tag in segment.iter_tags():
            if tag.entry.d_tag == "DT_SYMTAB":
                symtab_ptr = tag.entry.d_ptr
            if tag.entry.d_tag == "DT_SYMENT":
                assert symbol_size == tag.entry.d_val
            if tag.entry.d_tag == "DT_HASH":
                dthash_ptr = tag.entry.d_ptr

        stringtable = (
            segment._get_stringtable()  # pylint: disable=protected-access
        )

        symtab_offset = next(
            elf.address_offsets(symtab_ptr)  # type: ignore[no-untyped-call]
        )

        if dthash_ptr:
            # DT_SYMTAB provides no information on the number of symbols table
            # entries. Instead, we use DT_HASH's nchain value, which according
            # to the spec, "should equal the number of symbol table entries".
            # nchain is the second 32-bit integer at the address pointed by
            # DT_HASH, both for ELF and ELF64 formats.
            fmt = "<I" if elf.little_endian else ">I"
            nchain_offset = next(
                elf.address_offsets(  # type: ignore[no-untyped-call]
                    dthash_ptr + 4
                )
            )
            elf.stream.seek(nchain_offset)
            nsymbols = struct.unpack(fmt, elf.stream.read(4))[0]
        else:
            # Get the size of DYNSYM section from section header.
            symtab_size = int(GetSymbolTableSize(elf))
            nsymbols = symtab_size // symbol_size

        # The first symbol is always local undefined, unnamed so we ignore it.
        for i in range(1, nsymbols):
            symbol_offset = symtab_offset + (i * symbol_size)
            symbol = utils.struct_parse(  # type: ignore[no-untyped-call]
                elf.structs.Elf_Sym, elf.stream, symbol_offset
            )
            if symbol["st_info"]["bind"] == "STB_LOCAL":
                # Ignore local symbols.
                continue
            symbol_name = stringtable.get_string(symbol.st_name)
            if symbol["st_shndx"] == "SHN_UNDEF":
                if symbol["st_info"]["bind"] == "STB_GLOBAL":
                    # Global undefined --> required symbols.
                    # We ignore weak undefined symbols.
                    imp.add(symbol_name)
            elif symbol["st_other"]["visibility"] == "STV_DEFAULT":
                # Exported symbols must have default visibility.
                exp.add(symbol_name)

    return imp, exp


def ParseELF(
    root: Union[str, "os.PathLike[str]"],
    rel_path: Union[str, "os.PathLike[str]"],
    ldpaths: Optional[Dict[str, List[str]]] = None,
    parse_symbols: bool = False,
) -> Optional[Dict[str, Any]]:
    """Parse the ELF file.

    Loads and parses the passed elf file.

    Args:
        root: Path to the directory where the rootfs is mounted.
        rel_path: The path to the parsing file relative to root.
        ldpaths: The dict() with the ld path information. See
            lddtree.LoadLdpaths() for details.
        parse_symbols: Whether the result includes the dynamic symbols 'imp_sym'
            and 'exp_sym' sections. Disabling it reduces the time for large
            files with many symbols.

    Returns:
        None: If the passed file isn't a supported ELF file.
        dict: Otherwise, contains information about the parsed ELF.
    """
    # TODO(vapier): Convert to Path instead.
    root = str(root)
    rel_path = str(rel_path)

    # Ensure root has a trailing / so removing the root prefix also removes any
    # / from the beginning of the path.
    root = root.rstrip("/") + "/"

    with open(os.path.join(root, rel_path), "rb") as f:
        if f.read(4) != b"\x7fELF":
            # Ignore non-ELF files. This check is done to speedup the process.
            return None
        f.seek(0)
        # Continue reading and cache the whole file to speedup seeks.
        stream = io.BytesIO(f.read())

    try:
        elf = elffile.ELFFile(stream)  # type: ignore[no-untyped-call]
    except exceptions.ELFError:
        # Ignore unsupported ELF files.
        return None
    if elf.header.e_type == "ET_REL":
        # Don't parse relocatable ELF files (mostly kernel modules).
        return {
            "type": elf.header.e_type,
            "realpath": rel_path,
        }

    if ldpaths is None:
        ldpaths = lddtree.LoadLdpaths(root)  # type: ignore[no-untyped-call]

    result: Dict[str, Any] = lddtree.ParseELF(
        os.path.join(root, rel_path), root=root, ldpaths=ldpaths
    )  # type: ignore[no-untyped-call]
    # Convert files to relative paths.
    for libdef in result["libs"].values():
        for path in ("realpath", "path"):
            if not libdef[path] is None and libdef[path].startswith(root):
                libdef[path] = libdef[path][len(root) :]

    for path in ("interp", "realpath"):
        if not result[path] is None and result[path].startswith(root):
            # pylint: disable=unsubscriptable-object
            result[path] = result[path][len(root) :]

    result["type"] = elf.header.e_type
    result["sections"] = dict(
        (str(sec.name), sec["sh_size"])
        for sec in elf.iter_sections()  # type: ignore[no-untyped-call]
    )
    result["segments"] = set(
        seg["p_type"]
        for seg in elf.iter_segments()  # type: ignore[no-untyped-call]
    )

    # Some libraries (notably, the libc, which you can execute as a normal
    # binary) have the interp set. We use the file extension in those cases
    # because exec files shouldn't have a .so extension.
    result["is_lib"] = (
        result["interp"] is None or rel_path[-3:] == ".so"
    ) and elf.header.e_type == "ET_DYN"

    if parse_symbols:
        result["imp_sym"], result["exp_sym"] = ParseELFSymbols(elf)
    return result