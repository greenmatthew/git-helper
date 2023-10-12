from typing import Callable, List

class Command:
    command_dict = {}
    aliases_dict = {}

    def __init__(self, name: str, aliases: List[str], short_description: str, help_text: List[str], function: Callable):
        self.name = name
        self.aliases = aliases
        self.short_description = short_description
        self.help_text = help_text
        self.function = function

        # Add command to command dict
        Command.command_dict[self.name] = self

        # Add aliases to aliases dict
        for alias in aliases:
            Command.aliases_dict[alias] = self.name
    def short_help(self):
        print(f"{self.name.ljust(10)} {self.short_description}\n")

    def help(self):
        prefix = "usage: "
        prefix_length = len(prefix)
        # Handle the first line separately to add the prefix
        formatted_lines = f"{prefix}{self.help_text[0]}"
        # For the rest of the lines, prepend the appropriate number of spaces
        for line in self.help_text[1:]:
            formatted_lines += f"\n{' ' * prefix_length}{line}"
        print(formatted_lines)
    
    def execute(self, args: List[str]):
        if (not(args is None or len(args) == 0) and args[0] == "--help"):
            self.help()
            return
        else:
            self.function(args)
    
    help_command = None
    init_command = None