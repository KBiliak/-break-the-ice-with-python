# Write a program that accepts a sentence and calculate the number of upper
# case letters and lower case letters.
#
# Suppose the following input is supplied to the program:
#
# Hello world!
# Then, the output should be:
#
# UPPER CASE 1
# LOWER CASE 9

user_input = input("Enter a sentence and calculate the number of uppercase"
                   "letters and lower case letters\n")

uppercase_list = []
lowercase_list = []

def print_num_upper_lower(user_input):
    for upper in user_input:
        if upper.isupper():
            uppercase_list.append(upper)
    print(f"UPPER CASE {len(uppercase_list)}")

    for lower in user_input:
        if lower.islower():
            lowercase_list.append(lower)
    print(f"LOWER CASE {len(lowercase_list)}")


print_num_upper_lower(user_input)