import os

def clear():
    # Check the operating system
    if os.name == 'posix':
        # for Linux and macOS
        _ = os.system('clear')
    else:
        # for Windows
        _ = os.system('cls')
