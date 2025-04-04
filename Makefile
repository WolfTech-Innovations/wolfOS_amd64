# Optimized Makefile for ChromiumOS fork with wolfOS branding

TARGET = chromiumos
BRANCH = release-R60-9592.B

BOARD_ARM = arm-generic
BOARD_X86 = x86-generic
BOARD_X64 = amd64-generic

NPROC = $(shell nproc --all)
OUTPUT_DIR = $(PWD)/build/output
CHROOT_DIR = $(PWD)/chroot
BRANDING_DIR = ./branding
THEME_DIR = ./theme
REPO_URL = https://chromium.googlesource.com/chromiumos/manifest.git
REPO_TOOL_URL = https://storage.googleapis.com/git-repo-downloads/repo

export PATH := ${PWD}/depot_tools:${PATH}

all: setup branding images

# Ensure depot_tools is installed
depot_tools:
	@if [ ! -d depot_tools ]; then \
		git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git; \
	fi

# Setup ChromiumOS repo
setup: depot_tools ${TARGET}
	cd depot_tools && git pull origin --rebase
	cd ${TARGET} && repo sync -j${NPROC}
	-cd ${TARGET}/src && patch -p3 --forward < ${PWD}/update_bootloaders.sh.patch

${TARGET}: FORCE
	mkdir -p ${TARGET}
	cd ${TARGET} && repo init -u ${REPO_URL} -b ${BRANCH}

# Apply wolfOS branding
branding:
	@echo "Applying wolfOS branding..."
	@if [ -d "$(BRANDING_DIR)" ]; then cp -r $(BRANDING_DIR) ${TARGET}/src/platform/; fi
	@if [ -d "$(THEME_DIR)" ]; then cp -r $(THEME_DIR) ${TARGET}/src/platform/; fi

# Build all images
images: arm x86 x64

# Build process for each architecture
arm:
	cd ${TARGET} && cros_sdk -- ./setup_board --board=${BOARD_ARM}
	cd ${TARGET} && cros_sdk -- ./set_shared_user_password.sh chronos
	cd ${TARGET} && cros_sdk -- ./build_packages --board=${BOARD_ARM} --nowithdebug -j${NPROC}
	cd ${TARGET} && cros_sdk -- ./build_image --board=${BOARD_ARM} --noenable_rootfs_verification dev

x86:
	cd ${TARGET} && cros_sdk -- ./setup_board --board=${BOARD_X86}
	cd ${TARGET} && cros_sdk -- ./set_shared_user_password.sh chronos
	cd ${TARGET} && cros_sdk -- ./build_packages --board=${BOARD_X86} --nowithdebug -j${NPROC}
	cd ${TARGET} && cros_sdk -- ./build_image --board=${BOARD_X86} --noenable_rootfs_verification dev

x64:
	cd ${TARGET} && cros_sdk -- ./setup_board --board=${BOARD_X64}
	cd ${TARGET} && cros_sdk -- ./set_shared_user_password.sh chronos
	cd ${TARGET} && cros_sdk -- ./build_packages --board=${BOARD_X64} --nowithdebug -j${NPROC}
	cd ${TARGET} && cros_sdk -- ./build_image --board=${BOARD_X64} --noenable_rootfs_verification dev

# Virtual machine images
kvm: armk x86k x64k

armk:
	cd ${TARGET} && cros_sdk -- ./image_to_vm.sh --board=${BOARD_ARM}

x86k:
	cd ${TARGET} && cros_sdk -- ./image_to_vm.sh --board=${BOARD_X86}

x64k:
	cd ${TARGET} && cros_sdk -- ./image_to_vm.sh --board=${BOARD_X64}

# Distribution package creation
dist: armd x86d x64d armdk x86dk x64dk

distq: armdq x86dq x64dq

armd:
	cp ${TARGET}/src/build/images/${BOARD_ARM}/latest/chromiumos_image.bin ${OUTPUT_DIR}/chromiumos_image-${BOARD_ARM}.bin

x86d:
	cp ${TARGET}/src/build/images/${BOARD_X86}/latest/chromiumos_image.bin ${OUTPUT_DIR}/chromiumos_image-${BOARD_X86}.bin

x64d:
	cp ${TARGET}/src/build/images/${BOARD_X64}/latest/chromiumos_image.bin ${OUTPUT_DIR}/chromiumos_image-${BOARD_X64}.bin

# Convert raw images to QEMU format
armdq:
	qemu-img convert -f raw -O qcow2 ${TARGET}/src/build/images/${BOARD_ARM}/latest/chromiumos_qemu_image.bin ${OUTPUT_DIR}/chromiumos_qemu_image-${BOARD_ARM}.qcow2

x86dq:
	qemu-img convert -f raw -O qcow2 ${TARGET}/src/build/images/${BOARD_X86}/latest/chromiumos_qemu_image.bin ${OUTPUT_DIR}/chromiumos_qemu_image-${BOARD_X86}.qcow2

x64dq:
	qemu-img convert -f raw -O qcow2 ${TARGET}/src/build/images/${BOARD_X64}/latest/chromiumos_qemu_image.bin ${OUTPUT_DIR}/chromiumos_qemu_image-${BOARD_X64}.qcow2

# Cleanup commands
clean: FORCE
	cd ${TARGET} && cros_sdk --delete

distclean: clean FORCE
	cd ${TARGET} && cros_sdk --delete
	rm -rf depot_tools ${TARGET}

FORCE:
