# This program will showcase some of the string functions
favourite_music = "KPop Rocks"

print(f"The original string is: {favourite_music}")

favourite_music_upper = favourite_music.upper()
print(f"The upper case versions is: {favourite_music_upper}")

favourite_music_lower = favourite_music.lower()
print(f"The lower case verson is: {favourite_music_lower}")

favourite_music_title = favourite_music.title()
print(f"The title case version is: {favourite_music_title}")

length_of_favourite_music = len(favourite_music)
print(f"The length of the favourite music is: {length_of_favourite_music}")
#print(f"Type of length_of_favourite_music variable is: {type(length_of_favourite_music)}")

# original string is KPop Rocks
# the two numbers are start position and end position
first_few_characters = favourite_music[5:10]
print(first_few_characters)

# original string is KPop Rocks
# print everything from a particular position until the end
no_end_from_character = favourite_music[2:]
print(no_end_from_character)



favourite_music_list = favourite_music.split()
print(favourite_music_list)

# list of values or series of values
# it can be of any type
list_of_students = ['Anisa', 'Misby', 'Omer', 'Ammar']
print(list_of_students)

#Anisa Misby Omer Ammar
joined_list_of_students = " ".join(list_of_students)
print(joined_list_of_students)

#Anisa-Misby-Omer-Ammar
joined_list_of_students = "-".join(list_of_students)
print(joined_list_of_students)

#AnisaMisbyOmerAmmar
joined_list_of_students = "".join(list_of_students)
print(joined_list_of_students)


no_start_from_character = favourite_music[:2]
print(no_start_from_character)

full_from_character = favourite_music[:]
print(full_from_character)

skip_from_character = favourite_music[::2]
print(skip_from_character)

#if we put -1 as the positio of the character, then it will print
# the last character
last_from_character = favourite_music[-1]
print(last_from_character)

reverse_from_character = favourite_music[::-1]
print(reverse_from_character)
