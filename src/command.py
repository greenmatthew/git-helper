from typing import Callable, List

class Command:
    command_dict = {}
    aliases_dict = {}

    def __init__(self, name: str, aliases: List[str], help_text: str, function: Callable):
        self.name = name
        self.aliases = aliases
        self.help_text = help_text
        self.function = function

        # Add command to command dict
        Command.command_dict[self.name] = self

        # Add aliases to aliases dict
        for alias in aliases:
            Command.aliases_dict[alias] = self.name

    def help(self):
        print(self.help_text)
    
    def execute(self, args: List[str]):
        if (not(args is None or len(args) == 0) and args[0] == "--help"):
            self.help()
            return
        else:
            self.function(args)
    
    help_command = None
    init_command = None