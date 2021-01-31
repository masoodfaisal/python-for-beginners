# let's define a list of numbers
list_of_numbers = [5 ,6 ,7 ,8]

#print the full list
print(list_of_numbers)

#print the value at the second postion - becuase python starts couting at 0
print(list_of_numbers[1])

# define as start position : end position. Note that end position is NOT included
# this means that it will pick the number from position 1 and 2 and AVOID number at position 3
print(list_of_numbers[1:3])

print(list_of_numbers[:2])
print(list_of_numbers[2:])


list_of_students = ['Anisa', 'Misby', 'Omer']
print(list_of_students)

# Add item to the end of the list
list_of_students.append("Ammar")
print(list_of_students)

list_of_students.append("Faisal")
print(list_of_students)

# remove the mentioned item anywhere from the list
list_of_students.remove("Faisal")
print(list_of_students)

# Add the item to list at the given index
list_of_students.insert(2, "New Student")
print(list_of_students)

# a list of laptop manufacturers
list_of_computers = ["HP", "Apple", "Lenovo"]

# what if i want to add multiple manufacturer to the list above?
list_of_computers.extend(["Acer", "Asus", "Dell"])
print(list_of_computers)

list_of_computers.sort()
print(list_of_computers)

# lists can take multiple types of data
list_of_computers.append(True)
print(list_of_computers)

# find out how i can get the number of items in my list
# hint: the method name would be on the lines of COUNT













