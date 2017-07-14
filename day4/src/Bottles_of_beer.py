"""
Warm Up - OOP Practice

Create two (2) classes, Bar and Person.

Given a person and number of beers, countdown the number of beers until none are available.

Example:
    {Person.name}: '{Bar.beer.count()} bottles of {Bar.beer.name} on the wall, \n'
                   '{Bar.beer.count()} bottles of {Bar.beer.name}, \n'
                   'take one down pass them around, \n' \
                   '{Bar.beer.count() - 1}, \n'

Parameters:
    "Whats your name? " input()
    "What beer would you like? " input()
    "How many? " input()

Returns:
    Example
"""


class Bar:
    def __init__(self, stock=[]):
        self.stock = stock  # Start with an empty bar

    def stock(self, drink):
        self.stock.append(drink)  # Magically we have the drink in stock


class Person:
    def __init__(self, name, drink, beers):
        pass

    def sing(self):


# while


if __name__ == '__main__':
    # Get user input
    name = input("Whats your name? ")
    drink = input("What beer would you like? ")
    beers = input("How many? ")

    p = Person(name, drink, beers)
    b = Bar(drink)

    p.sing()
