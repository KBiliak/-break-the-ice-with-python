# Write a program that accepts a sentence and calculate the number of letters
# and digits.
#
# Suppose the following input is supplied to the program:
#
# hello world! 123
# Then, the output should be:
#
# LETTERS 10
# DIGITS 3

user_sentence = input("Enter your sentence to calculate the number of letters:"
                      "and digits.\n")
digits_list = []
letters_list = []
def calc_letters_digits(user_sentence):
    for digit in user_sentence:
        if digit.isdigit():
            digits_list.append(digit)
    print(f"DIGITS {len(digits_list)}")

    for letter in user_sentence:
        if letter.isalpha():
            letters_list.append(letter)
    print(f"LETTERS {len(letters_list)}")


calc_letters_digits(user_sentence)