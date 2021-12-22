import os
from pathlib import Path
from connectmp import __version__
from connectmp.core.utils import write_code_to_file
from connectmp.core.config import check_same_thread


def commandManager(args):
    """
    Built in cligo command manager.
    We call this in Terminal :
    C:/Some/Path> connectmp <some_command>
    """
    if not args:
        exit()

    if args[0] == "test":
        print(f"Test is Working. Arg: {args[0]}")

    elif args[0] == " --version":
        print(f"ConnectMP v{__version__}")

    elif args[0] == "config":
        if str(args[1]).lower() == "set":
            if args[2] == "check_same_thread":
                if str(args[3]).lower() == "true" or str(args[3]).lower() == "false":
                    file_path = os.path.join(Path(__file__).resolve().parent.parent, 'config.py')
                    s_code = f"check_same_thread = {str(args[3]).lower().capitalize()}"
                    write_code_to_file(source_code=s_code, file_path=file_path)
                    print(f"[ConnectMP]: (Config) - check_same_thread has been set to "
                          f"{str(args[3]).lower().capitalize()} ")

        elif str(args[1]).lower() == "get":
            if args[2] == "check_same_thread":
                print(f"[ConnectMP]: (Config) - check_same_thread={check_same_thread}")
