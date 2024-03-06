# Write a program that accepts sequence of lines as input and prints the
# lines after making all characters in the sentence capitalized.
#
# Suppose the following input is supplied to the program:
#
# Hello world
# Practice makes perfect
# Then, the output should be:
#
# HELLO WORLD
# PRACTICE MAKES PERFECT

print("Enter a sequence of lines: ")
lst = []
def printed_capitalized_lines():
    while True:
        user_input = input()
        if len(user_input) != 0:
            lst.append(user_input)
        else:
            print('\n'.join(lst).upper())
            break

printed_capitalized_lines()

