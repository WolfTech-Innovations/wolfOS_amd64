#!/bin/bash

# Build script for ChromeOS fork with wolfOS branding and theming
# Ensure this script is executed from the repository root

set -e

# Define variables
BUILD_ROOT=$(pwd)
OUTPUT_DIR="${BUILD_ROOT}/build/output"
CHROOT_DIR="${BUILD_ROOT}/chroot"
BOARD="amd64-generic"  # Replace with your specific target board
VERSION="1.0"          # Define your custom version
BRANDING_DIR="branding"  # Directory containing branding assets
THEME_DIR="theme"        # Directory containing color theming assets

mkdir -p ~/bin
curl -o ~/bin/repo https://storage.googleapis.com/git-repo-downloads/repo
chmod +x ~/bin/repo
export PATH=~/bin:$PATH
source ~/.bashrc

# Functions
function sync_sources() {
    echo "Syncing sources..."
    cd chromiumos
    repo init --depth=1 -u https://chromium.googlesource.com/chromiumos/manifest.git
    repo sync --jobs=4
    cd "${BUILD_ROOT}"
}

function apply_branding() {
    echo "Applying wolfOS branding..."
    if [ -d "${BRANDING_DIR}" ]; then
        cp -r "${BRANDING_DIR}"/* ChromiumOS/src/platform/*
        echo "Branding applied."
    else
        echo "Branding directory not found! Skipping branding step."
    fi
}

function apply_theming() {
    echo "Applying wolf color theming..."
    if [ -d "${THEME_DIR}" ]; then
        cp -r "${THEME_DIR}"/* ChromiumOS/src/platform/*
        echo "Theming applied."
    else
        echo "Theming directory not found! Skipping theming step."
    fi
}

function setup_chroot() {
    echo "Setting up chroot environment..."
    sudo ./ChromiumOS/chromite/bin/cros_sdk --bootstrap
}

function enter_chroot() {
    echo "Entering chroot and syncing..."
    sudo ./ChromiumOS/chromite/bin/cros_sdk -- ./setup_board --board="${BOARD}"
    sudo ./ChromiumOS/chromite/bin/cros_sdk -- ./update_chroot
}

function build_packages() {
    echo "Building packages for ${BOARD}..."
    sudo ./ChromiumOS/chromite/bin/cros_sdk -- ./build_packages --board="${BOARD}"
}

function build_image() {
    echo "Building image for ${BOARD}..."
    sudo ./ChromiumOS/chromite/bin/cros_sdk -- ./build_image --board="${BOARD}" --noenable_rootfs_verification
}

function move_output() {
    echo "Moving output to ${OUTPUT_DIR}..."
    mkdir -p "${OUTPUT_DIR}"
    cp -r "${CHROOT_DIR}/build/${BOARD}/latest" "${OUTPUT_DIR}"
    echo "Build artifacts stored in ${OUTPUT_DIR}"
}

# Main script
echo "Starting ChromeOS build process with wolfOS branding and theming..."

# Step 1: Sync sources
sync_sources

# Step 2: Apply wolfOS branding and theming
apply_branding
apply_theming

# Step 3: Set up chroot
setup_chroot

# Step 4: Enter chroot and prepare board
enter_chroot

# Step 5: Build packages
build_packages

# Step 6: Build the image
build_image

# Step 7: Move output to a safe directory
move_output

echo "Build process completed successfully with wolfOS branding and theming!"
