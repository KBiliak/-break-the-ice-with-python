# Write a program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.The
# numbers obtained should be printed in a comma-separated sequence on a single
# line.

first_num = 1000
second_num = 3000
list = []
def even_nums_in_range(first_num, second_num):
    num_range = range(first_num, second_num+1)
    for a in num_range:
        if a % 2 == 0:
            list.append(str(a))
    print(",".join(list))


even_nums_in_range(first_num, second_num)