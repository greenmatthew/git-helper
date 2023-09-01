from sys import argv, exit
from command import Command
from commands import initialize_commands

version="v0.1.0"

def help(args: list):
    print("""
MIT License, 2023, Matthew Green

git-helper v0.1.0
-----------------

Description:
------------
git-helper is a command-line utility designed to simplify the management of Git repositories. 
It's especially useful for handling repositories with multiple remotes, abstracting away the 
complexity of running multiple Git commands with a single, easy-to-use git-helper command.

Commands:
---------

help
    - Description: Displays all commands and their descriptions.
    
init [remote url]+
    - Description: Initializes a git repository with optional remote-URL pairs. 
                   Each remote should be followed immediately by its corresponding URL.


Usage:
------
git-helper <command> [options]

For more details on each command, use:
git-helper <command> --help
""")


def main(argc: int, argv: list):
    # Remove application run command
    argv = argv[1:]

    initialize_commands()

    try:
        command = argv.pop(0)
    except IndexError:
        Command.help_command.execute(argv)
        sys.exit(0)
    
    try:
        command = Command.command_dict[command]
    except:
        print(f"git-helper: '{command}' is not a valid command. If you need help try 'git-helper help'")
        Command.help_command.execute(argv)
        sys.exit(0)

    command.execute(argv)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
