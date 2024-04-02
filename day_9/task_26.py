"""Define a function which can generate a dictionary where the keys are
numbers between 1 and 20 (both included) and the values are square of keys.
The function should just print the keys only. """


def generate_dict():
    generated_dict = {}
    for i in range(1, 21):
        generated_dict[i] = i ** 2

    return generated_dict.keys()


hui = generate_dict()
print(hui)
