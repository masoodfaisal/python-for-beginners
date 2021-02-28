# # two parameters
# def sum(number1, number2):
#     sum = number1 + number2
#     print(sum)


def sum(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        sum = sum + number
    print(sum)

# define a function which can take multiple parameters
# Homework - Complete the function
def sum(number1, *args):
    # Homework, go through the type of MANY ARGUMENTS
    # print(type(args))
    for argument in args:
        print(argument)

sum(1,2)
sum(1,2,3)






list_of_numbers = [1,2,3]
sum(list_of_numbers)

list_of_numbers = [1,2,3,5,6,7]
sum(list_of_numbers)



# three parameters
# make a function that can take 3 numbers to SUM
# def sum(number1, number2, number3):
#     sum = number1 + number2 + number3
#     print(sum)


# four parameters


# def difference(number1, number2):
#     difference = number1 - number2
#     print(difference)

# def calculator(number1, number2, operation):
#     if operation == "+":
#         sum(number1, number2)
#     elif operation == "-":
#         difference(number1, number2)

# calculator(1, 2, "+")
# calculator(5, 3, "-")
