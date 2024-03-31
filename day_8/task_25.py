"""Define a function which can print a dictionary where the keys are numbers
between 1 and 20 (both included) and the values are square of keys. """

range_nums = range(1, 21)


def dict_with_square_keys():
    my_dict = {}
    for j in range_nums:
        my_dict[j] = j ** 2
    return my_dict


result = dict_with_square_keys()
print(result)
