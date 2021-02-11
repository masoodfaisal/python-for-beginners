# continue stops the current iteration and go back to the top of the loop
for number in range(5):
    # for a conditon go back 
    if number == 3:
        continue

    print(number)
    

# break stops the loop
for number in range(5):
    if number == 3:
        break
    print (number)

# I want ot print all the even number in the loop
for number in range(1, 10):
    remainder = number % 2
    if remainder != 0:
        continue
    print(number)



sample_number = 11
remainder = sample_number % 2
print(f"remainder is {remainder}")


# Write a program which takes a word as a user input
# The program will ONLY print the vowels in the word
# example: if I enter the word "hello", the program should print "eo"
