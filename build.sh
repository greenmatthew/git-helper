#!/bin/bash

# Variables
name="git-helper"
main_script="main.py"
source="src/"
output="output/"
build="build/"
specs="build/specs/"

# Create the output directory if it doesn't exist
mkdir -p "$output"
mkdir -p "$build"
mkdir -p "$specs"

# Compile to executable using PyInstaller
pyinstaller --onefile "$source/$main_script" --distpath="$output" --workpath="$build" --specpath="$specs" --name="$name"

# Ensure is can be executed
chmod +x "$output/$name"

# Add new compilation to /usr/local/bin so it is globally accessible
sudo cp "$output/$name" /usr/local/bin
echo "Moving $name to /usr/local/bin"
