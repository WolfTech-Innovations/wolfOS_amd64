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

# Variables
CPU_LIMIT="50000"    # CPU limit (50ms per 100ms, 50% usage)
MEMORY_LIMIT="2G"    # Memory limit (2GB)
CGROUP_NAME="global_limit"
CGROUP_PATH="/sys/fs/cgroup/$CGROUP_NAME"

# Function to check and install required tools
function install_tools() {
    local tools=("cpulimit" "util-linux" "cgroup-tools")
    echo "Checking and installing required tools..."
    for tool in "${tools[@]}"; do
        if ! command -v "$tool" &>/dev/null; then
            echo "Installing $tool..."
            if command -v apt &>/dev/null; then
                sudo apt update && sudo apt install -y "$tool"
            elif command -v yum &>/dev/null; then
                sudo yum install -y "$tool"
            elif command -v dnf &>/dev/null; then
                sudo dnf install -y "$tool"
            elif command -v pacman &>/dev/null; then
                sudo pacman -Sy "$tool"
            elif command -v zypper &>/dev/null; then
                sudo zypper install -y "$tool"
            else
                echo "Error: Package manager not found. Please install $tool manually."
                exit 1
            fi
        fi
    done
}

# Function to check cgroup version
function detect_cgroup_version() {
    if [[ $(stat -fc %T /sys/fs/cgroup/) == "cgroup2fs" ]]; then
        echo "Detected cgroup v2"
        return 2
    else
        echo "Detected cgroup v1"
        return 1
    fi
}

# Function to configure cgroup v2
function configure_cgroup_v2() {
    echo "Configuring cgroup v2..."
    sudo mkdir -p "$CGROUP_PATH"

    # Set CPU limit
    echo "Setting CPU limit..."
    echo "$CPU_LIMIT" | sudo tee "$CGROUP_PATH/cpu.max"

    # Set memory limit
    echo "Setting memory limit..."
    echo "$MEMORY_LIMIT" | sudo tee "$CGROUP_PATH/memory.max"

    # Attach all processes to the cgroup
    echo "Attaching all processes to the cgroup..."
    for pid in $(ps -e -o pid=); do
        echo "$pid" | sudo tee "$CGROUP_PATH/cgroup.procs" >/dev/null 2>&1
    done
    echo "Cgroup v2 configuration completed."
}

# Function to configure cgroup v1
function configure_cgroup_v1() {
    echo "Configuring cgroup v1..."
    sudo cgcreate -g cpu,memory:/$CGROUP_NAME

    # Set CPU limit
    echo "Setting CPU limit..."
    echo "$CPU_LIMIT" | sudo tee /sys/fs/cgroup/cpu/$CGROUP_NAME/cpu.cfs_quota_us
    echo "100000" | sudo tee /sys/fs/cgroup/cpu/$CGROUP_NAME/cpu.cfs_period_us

    # Set memory limit
    echo "Setting memory limit..."
    echo "$MEMORY_LIMIT" | sudo tee /sys/fs/cgroup/memory/$CGROUP_NAME/memory.limit_in_bytes

    # Attach all processes to the cgroup
    echo "Attaching all processes to the cgroup..."
    for pid in $(ps -e -o pid=); do
        sudo cgclassify -g cpu,memory:/$CGROUP_NAME "$pid" 2>/dev/null
    done
    echo "Cgroup v1 configuration completed."
}

# Main script logic
echo "Starting resource limit configuration..."

# Install required tools
install_tools

# Detect and configure cgroup version
detect_cgroup_version
CGROUP_VERSION=$?

if [[ $CGROUP_VERSION -eq 2 ]]; then
    configure_cgroup_v2
elif [[ $CGROUP_VERSION -eq 1 ]]; then
    configure_cgroup_v1
else
    echo "Error: Unable to detect cgroup version."
    exit 1
fi

echo "Global resource limits applied successfully!"
mkdir -p ~/bin
curl -o ~/bin/repo https://storage.googleapis.com/git-repo-downloads/repo
chmod +x ~/bin/repo
export PATH=~/bin:$PATH
source ~/.bashrc

# Functions
function sync_sources() {
    echo "Syncing sources..."
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
