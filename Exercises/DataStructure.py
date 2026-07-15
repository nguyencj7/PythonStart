# Python Data Stuctures #

# List #
# These are many List created List are cretaed with brackets [ ] #
grocery_list = ["eggs", "milk", "cheese", "pasta"]
odd_num = [1, 3, 5, 7, 9]
rand_list = ["egg", "tree", 3, "green", 94, "pluto", 3.14]

# Tuples on the other hand are created with parentheses ( ) and are immutable, meaning they cannot be changed after creation. Tuples are often used for fixed collections of items, such as the names of planets in our solar system.
planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")


# we are just using commments to disable the print statements below, you can uncomment them to see the output of the lists and tuples.

# print("The first item on the list is " + grocery_list[0])
# print("The second item on the list is " + grocery_list[1])
# print(planets[3])


# Sets #
# Sets are created with curly braces { } and are unordered collections of unique items. Sets are useful for removing duplicates from a list or for performing mathematical operations like union, intersection, and difference.
customers = {
    "James Smith", 
    "Andrea Richards", 
    "Sam Sharp", 
    "Brenda Logmire", 
    "Veronica March", 
    "Sylvia Smith", 
    "James Smith", 
    "Vanessa Bush", 
    "Steve Hammersmith", 
    "Brenda Logmire", 
    "Sylvia Smith", 
    "Steve Hammersmith", 
    "Walt Hawkins"
} 
# print(customers)

# Dictionaries #
# Dictionaries are created with curly braces { } and consist of key-value pairs. Each key is unique and maps to a specific value. Dictionaries are useful for storing and retrieving data based on a unique identifier.
customer1 = {
    "name": "James Smith",
    "age": 24,
    "Phone": "555-555-4928",
    "Email": "andrea@coffeeloversunite.us"
}
# print(customer1["name"])
customer3 = {
    "name": "Robert",
    "name": "John"
}
print(customer3)



# Boolean Variables #
# Boolean variables can only have two values: True or False. They are often used in conditional statements to control the flow of a program based on certain conditions.

walking = False
running = True

# Multidimensional Lists #
# Multidimensional lists are lists that contain other lists as their elements.
# They can be used to represent matrices or grids of data. Each inner list can be accessed using multiple indices.

# In this examplewe are using Daily High and Low Temperature (In Farenheit) 
temps = [
    [ 66, 34],
    [ 57, 25],
    [ 49, 45]
]

# Day 1 Temperatures #
print(temps[0])

# Day 2 Temperatures #
print(temps[1])

# Day 3 Temperatures #
print(temps[2])

# Day 1 High Temperature #
print(temps[0][0])

# Day 1 Low Temperature #
print(temps[0][1])
