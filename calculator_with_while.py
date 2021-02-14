"""" 
This program showcase the calcualtor wit the while loop.
it will exit if the user inout q
""" 

while True:
    # User input
    first_number = int(input("Please enter first number: "))
    second_number = int(input("Please enter second number:"))
    requested_operation = input("What do you want to do (+-*/ and q to exit): ")

    if requested_operation == "+":
        sum_of_numbers = first_number + second_number
        print("The sum is", sum_of_numbers)

    elif requested_operation == "-":
        difference_of_numbers = first_number - second_number
        print("The difference is", difference_of_numbers)

    elif requested_operation == "*":
        product_of_number = first_number * second_number
        print("The product is", product_of_number)

    elif requested_operation == "/":
        division_of_numbers = first_number - second_number
        print("The division is", division_of_numbers)

    elif requested_operation == "q":
         break   

    else:
        print("Please type a valid input. Valid inputs are +, -, *, / and q.")
        continue 

print("Thank you for using the calacualtor program")       
