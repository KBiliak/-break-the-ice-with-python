#Write a program which will find all such numbers which are divisible by 7 but
# are not a multiple of 5, between 2000 and 3200 (both included).The numbers
# obtained should be printed in a comma-separated sequence on a single line.


first_num = 2000
second_num = 3200

def div_by_7_not_div_by_5(first_num, second_num):
    for num in range(first_num, second_num):
        if num % 7 == 0 and num % 5 != 0:
            yield str(num)


res_gen = div_by_7_not_div_by_5(first_num, second_num + 1)
print(", ".join(res_gen))

