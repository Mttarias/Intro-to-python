#1 What is the difference between a tuple and a list?
# A List is a collection of variables that can be modified, tuple is like a list but cannot be modified. While lists seem more enticing due to this fact, arguments can be made for
#tuples as they can be iterated through quicker and takes up less space in memory compared to lists.

#2 How is a list different than a dictionary?
# Dictionaries hold a key-value pair of variables, whereas a list only holds single value variables. This lets the user designate the key to access the variable/value, in a list
#the user must use index of the list starting at the integer 0. A dictionary is once again faster and takes up less space in memory.

#3 Create a program that prints a list of words in random order. The program should print all the words and not repeat any.
import random

tupleWords = ("apples", "zebra", "mountain", "chip", "monty", "beanstalk", "moon")
listWords = []

while len(listWords) is not len(tupleWords):
    word = random.choice(tupleWords)
    if word in listWords:
        continue
    else :
        print(word)
        listWords.append(word)

#4 Write a Character Creator program for a role-playing game. The player should be given a pool of 30 points to spend on four attributes: Strength, Health, Wisdom, and Dexterity.
#  The player should be able to spend points from the pool on any attribute and should also be able to take points from an attribute and put them back into the pool.
attributes = {"Strength": 0, "Health": 0, "Wisdom": 0, "Dexterity": 0}
points = 30

while True:
    print("1. Add points\n2. Remove Points\n3. Display attributes and points\n4. Exit")
    menu = int(input("Please choose an option: "))
    
    if menu is 1:

        for key in attributes:
            print(key)

        attributeChoice = input("type the attribute you wish to add points to: ")
        if attributeChoice.lower().capitalize() not in attributes:
            print("Chosen attribute is not one of the four available.")
            continue

        numberOfPoints = int(input("How many points would you like to add? "))
        if numberOfPoints > points:
            print("Not enough points available.")
            continue

        currentPoints = attributes[attributeChoice.lower().capitalize()]
        attributes[attributeChoice.lower().capitalize()] = numberOfPoints + currentPoints
        points -= numberOfPoints
    
    elif menu is 2:

        for key in attributes:
            print(key)

        attributeChoice = input("type the attribute you wish to remove points from: ")
        if attributeChoice.lower().capitalize() not in attributes:
            print("Chosen attribute is not one of the four available.")
            continue
        
        currentPoints = attributes[attributeChoice.lower().capitalize()]
        numberOfPoints = int(input("How many points would you like to remove? "))
        if numberOfPoints > currentPoints:
            print("Not enough points available to remove.")
            continue

        attributes[attributeChoice.lower().capitalize()] = numberOfPoints - currentPoints
        points += numberOfPoints

    elif menu is 3:

        print(attributes)
        print("Points left to spend: ", str(points))

    elif menu is 4:

        print("exiting")
        break

    else:
        print("Not a valid choice.")

#5 Write a Who’s Your Daddy? program that lets the user enter the name of a male and produces the name of his father. 
# (You can use celebrities, fictional characters, or even historical figures for fun.) Allow the user to add, replace, and delete son-father pairs.

fathers = ("Abraham Lincoln", "Brandon Sanderson", "Albert Einstein", "John F. Kennedy", "Gilgamesh", "Monkey D. Luffy", "Joe Abercrombie", "Timothee Chalamet", "Leonardo DiCaprio", "Genghis Khan")

pairs = {}

while True:
    print("1. Add/replace son-father pair\n2. Remove pair\n3. Display pairs\n4. Exit")
    menu = int(input("Please choose an option: "))
    
    if menu is 1:

        son = input("Enter the name of the son: ")
        
        pairs.update({son : random.choice(fathers)})
    
    elif menu is 2:

        son = input("Enter the name of the son you wish to remove from the pairs: ")

        pairs.pop(son)

    elif menu is 3:

        print(pairs)

    elif menu is 4:

        print("exiting")
        break

    else:
        print("Not a valid choice.")