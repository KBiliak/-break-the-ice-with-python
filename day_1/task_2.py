# Write a program which can compute the factorial of a given numbers.The
# results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output
# should be:40320

def fact(x):
    res_list = []

    for num in range(x):
        res_list.append(num) # [0, 1, 2, 3, 4, 5, 6, 7]

    i = 1
    for value in res_list:
        value *= i # 0 * 1, 1 * 1, 6 * 3, 96, 5 * 120, 6 * 720, 5040 * 7
        i += value # (0 + 1), (1 + 1), (18 + 6), (24 +96) + (600 + 120) + (4320 + 720) + (35280 + 5040)
        yield str(i) #1, 2, 6, 24, 120, 720, 5040, 40320

fact = fact(8)
print(", ".join(fact))
