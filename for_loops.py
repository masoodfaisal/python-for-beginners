#for loop

list_of_students = ["Anisa", "Misby", "Omer", "Ammar"]
print(list_of_students)

for student in list_of_students:
    print(student)
    print(f"Student is {student}")
    print("Student")

print("Last Student")

prime_numbers = [1,2,3,5,7,11,13]
for number in prime_numbers:
    print(number)

# I know the number of family members for a group of families is
# and i wanna count how many total persons i know 
list_of_family_members = [4, 6, 5, 3, 10]
# total_family_members =  list_of_family_members[0] + \
#                         list_of_family_members[1] + \
#                         list_of_family_members[2] + \
#                         list_of_family_members[3]
# print(f"The number of people I know is : {total_family_members}")


# start with 0
# sum the previous value with the first element of the list
# 0 + 4 = 4
# sum the previous value with the second element of the list
# 4 + 6 = 10
# sum the previous value with the thrid element of the list
# 10 + 5 = 15
# sum the previous value with the fourht element of the list
# 15 + 3 = 18
total_family_members = 0
for family_member in list_of_family_members:
    total_family_members = total_family_members + family_member

print(f"Total number of people I know is {total_family_members}")

print("## Range ##")
# print(f"Range is {range(2)}")
# for i in range(5):
#     print(i)

# for i in range (10, 20):
#     print(i)

# range has start(i.e. 10), stop (i.e. 20) and the increment (i.e. 2) is
# as shown below
for i in range (10, 20, 2):
    print(i)

print("Enumerate")
prime_numbers = [1,2,3,5,7,11,13]
# 1 is at location 1
# 2 is at locaton 2
# 3 is at locaton 3
# 5 is at location 4
# Homework - do it with the fol loop (home work)


# easier is
for location, prime_number in enumerate(prime_numbers):
    print(f"{prime_number} is at location {location}")


# Homwwork - find the highest number in a list of numbers


