# Write a program which accepts a sequence of comma-separated numbers from
# console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
#
# 34,67,55,33,12,98
# Then, the output should be:
#
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

user_input = input("Enter a sequence of comma-separated numbers: ").split(",")


def generate_list_tuple(user_input):

    generated_list = list(user_input)
    generated_tuple = tuple(user_input)

    return generated_list, generated_tuple


generated_list, generated_tuple = generate_list_tuple(user_input)
print(generated_list)
print(generated_tuple)

