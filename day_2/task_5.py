# Question:
# Define a class which has at least two methods:
#
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class Request_Handler:

    def getString(self):
        self.user_string = input("Enter your question: ")

    def printString(self):
        print(self.user_string.upper())


request = Request_Handler()

request.getString()
request.printString()

