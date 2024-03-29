# With a given integral number n, write a program to generate a dictionary that
# contains (i, i x i) such that is an integral number between 1 and n (both
# included). and then the program should print the dictionary.Suppose the
# following input is supplied to the program: 8
#
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


def dict_generator(x):
    dict_result = {}
    key_ = range(1, x + 1)
    for key, value in enumerate(key_, start=1):
        val = value * value
        dict_result[key] = val
    print(dict_result)


dict_generator(8)
