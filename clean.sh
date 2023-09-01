#!/bin/bash

# Variables
build="build/"
specs="build/specs"

# Remove the build and specs directories
rm -rf "$build" "$specs"

echo "Cleaned build and specs directories."
