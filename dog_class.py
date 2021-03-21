# dog has following properties:
# name
# age
# type


class Dog:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def sit(self):
        print(f"The dog {self.name} is now sitting")    

    def puppy(self):
        if(self.age < 6):
            print(f"The dog {self.name} is a puppy")
        else:
            print(f"The dog {self.name} is a NOT puppy")

bull_dog = Dog("William", 3, "bulldog")
chowawa = Dog("Lucy", 7, "chowawa")
list_of_dogs = [bull_dog, chowawa]

# bull_dog.puppy()
chowawa.puppy()

# EXercise: 
#What are the three properties I can have in my House object
# Ammar : Model, company, type e.g. # Omer: company, type, year e.g company:  Richcraft    type:   Wildwood    year:  2021
# Misbah: model, type, price e.g.  model: spoke, type: semi-house, price: 900k
# Omer: company, type, year e.g company:  Richcraft    type:   Wildwood    year:  2021
# Anisa: model, type, price e.g.  Colour : Red      Age : 12      Type : Semi-house

# What are the three properties I can have in my Restaurant object
# Ammar : name, rating, location e.g. name : Chia Malaysia, 4.5 stars , 44 dixon Rd.
# Misbah: location, name, age e.g. Cana, Fountain Rd, 4 years old
# Omer: name, location, food e.g. McDonalds, 10000000 Something Street, Rice
# Anisa: food, place, name e.g. Food : Canadian        Place : Whitby         Name : McDonalds

# HOwework is. DEfine the REstaurant and House objects and dfine at least two action on them
