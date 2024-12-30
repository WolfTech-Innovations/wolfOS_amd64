#!/bin/bash

# Common setup for building ChromiumOS

# Exit on errors
set -e

# Define the root directory of the ChromiumOS source
CROS_DIR=$(pwd)

# Ensure the script is being run from the correct directory
if [ ! -d "$CROS_DIR" ]; then
  echo "This script must be run from the ChromiumOS root directory."
  exit 1
fi

# Function to set up the build environment
function setup_build() {
  echo "Setting up build environment..."
  
  # Example environment variable for build
  export USE_CCACHE=1
  export CCACHE_DIR="$CROS_DIR/.ccache"
  export GOMA_DIR="$CROS_DIR/.goma"
  
  # More setup logic, like creating necessary directories
}

# Function to clean up the environment
function clean_up() {
  echo "Cleaning up build environment..."
  
  # Example cleanup logic
  rm -rf "$CROS_DIR/out"
  rm -rf "$CROS_DIR/.ccache"
}

# Function to start the build process
function start_build() {
  echo "Starting the build process..."
  export BOARD=amd64-generic
  export CHROMEOS_RELEASE_TRACK="stable-channel"
  export CHROMEOS_RELEASE_BOARD="amd64-generic"
  export HOME_URL="https://wolfos.pages.dev/" 
  export NAME="wolfOS" 
  ../bin/build_packages --nohooks --board={BOARD}
}

# Main function to handle command-line arguments and run the appropriate tasks
case "$1" in
  setup)
    setup_build
    ;;
  clean)
    clean_up
    ;;
  build)
    start_build
    ;;
  *)
    echo "Usage: $0 {setup|clean|build}"
    exit 1
    ;;
esac

exit 0
