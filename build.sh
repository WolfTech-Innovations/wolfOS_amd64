#!/bin/bash

# Build script for ChromeOS fork with wolfOS branding and theming
# Ensure this script is executed from the repository root

set -e

# Define variables
BUILD_ROOT=$(pwd)
OUTPUT_DIR="$BUILD_ROOT/build/output"
CHROOT_DIR="$BUILD_ROOT/chroot"
BOARD="amd64-generic"  # Replace with your specific target board
VERSION="1.0"
BRANDING_DIR="./branding"
THEME_DIR="theme"

# Check for necessary tools and install missing ones
function install_tools() {
    local tools=("git" "curl" "python3" "build-essential")
    echo "Checking and installing required tools..."
    for tool in "${tools[@]}"; do
        if ! command -v "$tool" &>/dev/null; then
            echo "Installing $tool..."
            sudo apt update && sudo apt install -y "$tool"
        fi
    done
}

# Ensure repo is available
if [ ! -f ~/bin/repo ]; then
    mkdir -p ~/bin
    curl -o ~/bin/repo https://storage.googleapis.com/git-repo-downloads/repo
    chmod +x ~/bin/repo
    export PATH=~/bin:$PATH
fi

# Sync sources efficiently
function sync_sources() {
    echo "Syncing sources..."
    mkdir -p ChromiumOS
    cd ChromiumOS
    if [ ! -d .repo ]; then
        repo init --depth=1 -u https://github.com/karfield/chromiumos-manifest.git -b stabilize-9000.84.B
    fi
    repo sync --jobs=$(nproc --all) --quiet
    cd "$BUILD_ROOT"
}

# Apply wolfOS branding and theming
function apply_customizations() {
    echo "Applying wolfOS branding and theming..."
    [[ -d "$BRANDING_DIR" ]] && cp -r "$BRANDING_DIR"/* ChromiumOS/src/platform/
    [[ -d "$THEME_DIR" ]] && cp -r "$THEME_DIR"/* ChromiumOS/src/platform/
}

# Build steps
function setup_chroot() { sudo ./ChromiumOS/chromite/bin/cros_sdk --bootstrap; }
function enter_chroot() { sudo ./ChromiumOS/chromite/bin/cros_sdk -- ./setup_board --board="$BOARD"; }
function build_packages() { sudo ./ChromiumOS/chromite/bin/cros_sdk -- ./build_packages --board="$BOARD"; }
function build_image() { sudo ./ChromiumOS/chromite/bin/cros_sdk -- ./build_image --board="$BOARD" --noenable_rootfs_verification; }

# Move output
function move_output() {
    mkdir -p "$OUTPUT_DIR"
    cp -r "$CHROOT_DIR/build/$BOARD/latest" "$OUTPUT_DIR"
    echo "Build artifacts stored in $OUTPUT_DIR"
}

# Main script execution
echo "Starting ChromeOS build process with wolfOS branding and theming..."
install_tools
sync_sources
apply_customizations
setup_chroot
enter_chroot
build_packages
build_image
move_output
echo "Build process completed successfully!"
