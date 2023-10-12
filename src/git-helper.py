from sys import argv, exit
from commands.command import Command
from commands.commands import initialize_commands

version="v0.1.0"

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
