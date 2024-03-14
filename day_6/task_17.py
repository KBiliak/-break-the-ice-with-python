"""Write a program that computes the net amount of a bank account based a transaction
log from console input. The transaction log format is shown as following:
D 100; W 200 (D means deposit while W means withdrawal.)
Suppose the following input is supplied to the program: D 300; D 300; W 200; D 100 Then, the output should be: 500"""
def compute_net_amount():
    amount = 0
    list_amount = []

    while True:
        try:
            user_input = input(
                "choose D to deposit or W to withdrawal, If you want to exit, "
                "enter 'E': ").title()

            if user_input == "D":
                amount_input = int(input("enter a sum: "))
                sum_amount = amount_input + amount
                list_amount.append(sum_amount)
                print(sum(list_amount))

            if user_input == 'W':
                amount_input = int(input("enter a summa: "))
                min_amount = amount - amount_input
                list_amount.append(min_amount)
                print(sum(list_amount))

            if user_input == 'E':
                break

        except ValueError:
            print("Enter a number")


compute_net_amount()

