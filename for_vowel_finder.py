###########
"""
Build a code that request a word from the user and return how many vowels that
word contains.
"""

# Ask user for the input
# we know that this is going to be input function
word = input("Please enter a word: ")

# Define a variable to store the number of vowels found in the word
number_of_vowels = 0

# to find the number of vowels in a word, i need to go through each and every letter in the word
# i will LOOP through the letters in the word
for letter in word:
    # print(letter)
    
    # once i get the first letter, i will compare it and see if it is a vowel
    # i will use CONTROL STRUCTURE to compare the letter with the first element/letter
    if letter == "a":
        # whenever the letter is vowel, I will update my variable which store the number of vowels found
        # by 1
        number_of_vowels = number_of_vowels + 1
# at the end my variable will have th number of vowels

print(f"Total number of A is {number_of_vowels}")
