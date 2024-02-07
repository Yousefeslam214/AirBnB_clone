#!/usr/bin/python3
import cmd
import sys
# (Cmd) help
# Documented commands (type help <topic>):
# ========================================
# greet  help
# Undocumented commands:
# ======================
# EOF

# (Cmd) help greet
# greet [person]
#         Greet the named person

class MyConsole(cmd.Cmd):

    def precmd(self, line):
        #make the app work non-interactively
        if not sys.stdin.isatty():
            print()
        #print(line)
        if "." in line:
            line = line.replace(".", " ").replace("(", "").replace(")", "")
            line = line.split(" ")
            line = f"{line[1]} {line[0]}"
        print(line)
        
        #command , other= line.split(" ")
        #line = f"{command} shoes"
        return cmd.Cmd.precmd(self, line)

    def do_create(self, line):
        """greet [line]
        Greet the named line"""
        if line:
            print("i have a", line)
        else:
            print('hi')

    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print("hi,", person)
        else:
            print('hi')

    def do_EOF(self, line):
        return True

    def postloop(self):
        print()

if __name__ == "__main__":
    MyConsole().cmdloop()
