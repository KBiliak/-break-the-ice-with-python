# Write a program that accepts a sequence of whitespace separated words as
# input and prints the words after removing all duplicate words and sorting
# them alphanumerically.
#
# Suppose the following input is supplied to the program:
#
# hello world and practice makes perfect and hello world again
# Then, the output should be:
#
# again and hello makes perfect practice world


user_input = input("please enter a sequence of separated words \n").split()
my_set = set()
my_set.add(user_input[0])

for word in user_input:
    if word not in my_set:
        my_set.add(word)

sorted_order = sorted(my_set)
print(' '.join(sorted_order))


