# User input
# This program calculate the sum or difference of two numbers
# The numbers are enetered by the user

# descriptijve names of the variables
first_number = int(input("Please enter first number: "))
second_number = int(input("Please enter second number: "))
requested_operation = input("What do you want to do (+/-): ")

#Get the value from requested operation variables and apply the condition 
# to calcualte sum or differemce
if requested_operation == "+":
    sum_of_numbers = first_number + second_number
    print(f"The sum is {sum_of_numbers}")
elif requested_operation == "-":
    difference_of_numbers = first_number - second_number
    print("The difference is", difference_of_numbers)
else: 
    print("Not the valid input")

print("Thank you for using my calculator")

# - SUBTRACTION
# * MULTIPLE
# / DIVISION

# The output format is "The sum is NUMBER"

