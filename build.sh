#!/bin/bash

# Build script for ChromeOS fork
# Ensure this script is executed from the repository root

set -e

# Define variables
BUILD_ROOT=$(pwd)
OUTPUT_DIR="${BUILD_ROOT}/output"
CHROOT_DIR="${BUILD_ROOT}/chroot"
BOARD="amd64-generic" # Replace with your specific target board
VERSION="1.0"         # Define your custom version

# Functions
function setup_chroot() {
    echo "Setting up chroot environment..."
    sudo ./ChromiumOS/chromite/bin/cros_sdk --create --replace
}

function enter_chroot() {
    echo "Entering chroot and syncing..."
    sudo ./ChromiumOS/chromite/bin/cros_sdk -- ./setup_board --board="${BOARD}"
    sudo ./ChromiumOS/chromite/cros_sdk -- ./update_chroot
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

function clean_up() {
    echo "Cleaning up..."
    sudo ./ChromiumOS/chromite/bin/cros_sdk -- ./clean_chroot
}

# Main script
echo "Starting ChromeOS build process..."

# Step 1: Set up chroot
setup_chroot

# Step 2: Enter chroot and prepare board
enter_chroot

# Step 3: Build packages
build_packages

# Step 4: Build the image
build_image

# Step 5: Move output to a safe directory
move_output

# Step 6: Cleanup
clean_up

echo "Build process completed!"
