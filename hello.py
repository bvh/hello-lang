#
# Hello Language
#
# First step: A simple REPL (Read, Evaluate, Print, and Loop). We READ a line
# of user input with the `input` statement, EVALUATE the line, looking for the
# one (and currently, only) recognized keyword with the `if` statement, PRINT
# the results, and wrap it all in an infinite LOOP.
#

while (True):
    line = input("? ")
    if line.strip() == "bye":
        print("Bye.")
        break
    print(line)
