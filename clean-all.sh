#!/bin/bash

# Variables
build="build/"
specs="build/specs"
output="output/"

# Remove the build, specs, and output directories
rm -rf "$build" "$specs" "$output"

echo "Cleaned build, specs, and output directories."
