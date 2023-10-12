NAME="git-helper"
MAIN_SCRIPT="$(NAME).py"
SOURCE="src/"
OUTPUT="output/"
BUILD="build/"
SPECS="build/specs/"

build:
	@# Create the output directory if it doesn't exist
	@mkdir -p "$(OUTPUT)"
	@mkdir -p "$(BUILD)"
	@mkdir -p "$(SPECS)"

	@# Compile to executable using PyInstaller
	@pyinstaller --onefile "$(SOURCE)/$(MAIN_SCRIPT)" --distpath="$(OUTPUT)" --workpath="$(BUILD)" --specpath="$(SPECS)" --name="$(NAME)"

	@# Ensure is can be executed
	@chmod +x "$(OUTPUT)$(NAME)"

	@# Add new compilation to /usr/local/bin so it is globally accessible
	@sudo cp "$(OUTPUT)$(NAME)" /usr/local/bin
	@echo "Moving $(NAME) to /usr/local/bin"

run: build
	@./$(OUTPUT)$(NAME)

clean:
	@# Remove the build and specs directories
	@rm -rf "$(BUILD)" "$(SPECS)"

	@echo "Removed build directory."
	@echo "Removed specs directory."

cleanall: clean
	@# Remove the build, specs, and output directories
	@rm -rf "$(OUTPUT)"

	@echo "Removed output directory."

.PHONY: build run clean cleanall