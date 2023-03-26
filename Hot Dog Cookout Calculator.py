#Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers.
#The program should ask the user for the number of people attending the cookout and the number of hot dogs each person will be given.
#Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8.
#The program should display the following details:

#• The minimum number of packages of hot dogs required
#• The minimum number of packages of hot dog buns required
#• The number of hot dogs that will be left over
#• The number of hot dog buns that will be left over
import math

HOT_DOG = 10
HOT_DOG_BUN = 8

peopleAttending = int(input("How many people are attending the cookout? "))

hotdogsPerPerson = int(input("How many hot dogs will each person be given? "))

totalHotdogs = peopleAttending * hotdogsPerPerson

minimumDogs = math.ceil(totalHotdogs / HOT_DOG)
leftoverDogs = HOT_DOG - (totalHotdogs % HOT_DOG)

minimumBuns = math.ceil(totalHotdogs / HOT_DOG_BUN)
leftoverBuns = HOT_DOG_BUN - (totalHotdogs % HOT_DOG_BUN)

print("Minimum number of packages of hot dogs required:", minimumDogs)
print("leftover number of packages of hot dogs:", leftoverDogs)
print("Minimum number of hot dog buns required:", minimumBuns)
print("leftover number of hot dog buns:", leftoverBuns)