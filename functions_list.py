# a function calculates the sqaure of the list
def squares(numbers):
    for number in numbers:
        square = number * number
        print(f"The square of {number} is {square}")


list_of_numbers = [2, 5, 10]
squares(list_of_numbers)


second_list_of_numbers = [20, 50, 100]
squares(second_list_of_numbers)


# Home Work 3
# Write a function that can take a list of numbers and print the highest number
# the name of the function should be find_maximum_number and it can take a list as parameter