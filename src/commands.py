from typing import Callable, List
from command import Command
import os
import shutil
import git

def help_function(args: List[str]):
    print("""MIT License, 2023, Matthew Green

git-helper v0.1.0
-----------------

Description:
------------
git-helper is a command-line utility designed to simplify the management of Git repositories. 
It's especially useful for handling repositories with multiple remotes, abstracting away the 
complexity of running multiple Git commands with a single, easy-to-use git-helper command.

Commands:
---------""")
    
    for command in Command.command_dict.values():
        if command is not None:
            command.help()
            print("\n")
    
    print("""Usage:
------
git-helper <command> [options]

For more details on each command, use:
git-helper <command> --help""")

def delete_dir(path: str):
    if os.path.isdir(path):
        shutil.rmtree(path)

def init_function(args: List[str]):
    cwd = os.getcwd()
    delete_repo = lambda: delete_dir(f"{cwd}/.git")
    repo = git.Repo.init(cwd)

    remotes = []

    last_arg = None
    while len(args) != 0:
        arg = args.pop(0)

        if (arg == "--remote"):
            try:
                remote_name = args.pop(0)
            except IndexError:
                print("--remote is missing remote name")
                delete_repo()
                return
            
            try:
                remote_url = args.pop(0)
            except IndexError:
                print("--remote is missing remote URL")
                delete_repo()
                return
            
            remotes.append((remote_name, remote_url))
            last_arg = arg
        else:
            print(f"git-helper init: '{arg}' is an unknown option.")
            delete_repo()

            if last_arg == "--remote":
                print(f"Maybe you are missing another '--remote'?")

            return
    
    include_all_remote = len(remotes) > 1
    for index, (name, url) in enumerate(remotes):
        try:
            repo.create_remote(name, url)
        except:
            delete_repo()
            return

        if include_all_remote:
            if index == 0:
                try:
                    repo.create_remote("all", url)
                except:
                    delete_repo()
            try:
                repo.git.execute(["git", "remote", "set-url", "--add", "--push", "all", url])
            except:
                delete_repo()

def initialize_commands():
    Command.help_command = Command(
    name = "help",
    aliases = ["--help"],
    help_text = """help
    - Description: Displays all commands and their descriptions.""",
    function = help_function
    )

    Command.init_command = Command(
    name = "init",
    aliases = [],
    help_text = """init [remote url]+
    - Description: Initializes a git repository with optional remote-URL pairs. 
                   Each remote should be followed immediately by its corresponding URL.""",
    function = init_function
    )
