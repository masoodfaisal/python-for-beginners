# User input
first_number = float(input("Please enter first number: "))
second_number = int(input("Please enter second number:"))
sum_of_numbers = first_number + second_number

# - SUBTRACTION
# * MULTIPLE
# / DIVISION

print("Type of the number is ", type(first_number))

# The output format is "The sum is NUMBER"
print("The sum is", sum_of_numbers)

# The output format is as follows
# "The sum of FIRST_NUMBER and SECOND_NUMBER is NUMBER"
# print("The sum of", first_number, "and", second_number, "is", sum_of_numbers)
print(f"The sum of {first_number} and {second_number} is {sum_of_numbers}")