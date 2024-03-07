# Write a program which accepts a sequence of comma separated 4 digit binary
# numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated
# sequence.
#
# Example:
#
# 0100,0011,1010,1001,1111
# Then the output should be:
#
# 1010,1111

print("Enter a binary number: ")
user_input = input().split(',')

lst = []


def div_by_5(user_input):
    try:
        for digit in user_input:
            decimal_equivalent = int(digit, 2)
            if decimal_equivalent % 5 == 0:
                lst.append(digit)

        print(','.join(lst))

    except ValueError as err:
        print(err)


div_by_5(user_input)
