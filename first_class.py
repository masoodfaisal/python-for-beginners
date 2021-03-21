# item has following properts:
# name
# price
# color

# dog has following properties:
# name
# type

# car has followig properties:
# make
# model
# year

# e.g. car, item and dog are called an object

## DEfine a Car object
class Car:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


# instance of an object
audi = Car("audi", "a4", 2020)
camry = Car("toyota", "camry", 2019)


print(f"The model of my car is {audi.model}")


# HOmework
# Define an object for item



