# create a calculate function that can do addition and subtraction
# define a fucntion name as calculator, with three input paramaters. Two paramaters are the numbers and the third paramter is the operation
def calculator(number1, number2, operation):
    if operation == "+":
        sum(number1, number2)
    elif operation == "-":
        difference(number1, number2)


def sum(number1, number2):
    sum_of_numbers = number1 + number2
    print(f"The sum of {number1} and {number2} is {sum_of_numbers}")

def difference(number1, number2):
    diff_of_numbers = number1 - number2
    print(f"The difference of {number1} and {number2} is {diff_of_numbers}")

calculator(1, 2, "+")



#Home Work 1
# Build a complete calculator function that can take two numbers from users as inout and operation to perform on those numbers

#Home Work 2
# Build a calculator program that can a LIST of numbers and perform an operation on those numbers
# e.g. user can input: 1,3,5 and operation as +, then the pg=rogram will print 9
