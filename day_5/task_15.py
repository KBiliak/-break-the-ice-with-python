# Write a program that computes the value of a+aa+aaa+aaaa with a given digit
# as the value of a.
#
# Suppose the following input is supplied to the program:
#
# 9
# Then, the output should be:
#
# 11106
list_of_values = []

user_num = input("Please, enter your number: ")
for i in range(1, 5):
    values = int(i * user_num)
    list_of_values.append(values)


print(sum(list_of_values))