#!/usr/bin/env python3

import textwrap

def cowsay(message):
    wrapped = textwrap.fill(message, width=40)
    lines = wrapped.splitlines()
    width = max(len(line) for line in lines)
    top = " " + "_" * (width + 2)
    bottom = " " + "-" * (width + 2)
    bubble = "\n".join(f"< {line.ljust(width)} >" for line in lines)
    cow = r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
    """
    return f"{top}\n{bubble}\n{bottom}\n{cow}"

def main():
    print("Welcome to CowShell! Type a message and press Enter.\n")
    try:
        while True:
            msg = input("🐄 > ")
            if msg.strip().lower() in ('exit', 'quit'):
                break
            print(cowsay(msg))
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")

if __name__ == "__main__":
    main()
