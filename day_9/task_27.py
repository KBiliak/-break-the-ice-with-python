"""With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first
 half values in one line and the last half values in one line."""


def print_half_in_1_line():
    half = int(len(given_tuple) / 2)
    print(given_tuple[:half])
    print(given_tuple[half:])


given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

print_half_in_1_line()
