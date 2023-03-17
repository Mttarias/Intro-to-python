
#1. Write a Python program that prints (displays) your name, address, and telephone number.
print("Matt Berr\n123 Overyonder st\nBarcelona, Spain\n555-8080")

#2. Write and test a program that computes the area of a circle. This program should request a number representing the radius as input from the user. 
#   It should use the formula 3.14 * radius ** 2 to compute the area and then output this result suitably labeled.
radius = int(input("Please enter the radius of the circle: "))
area = 3.14 * (radius ** 2)
print("Area of the circle, based on radius", radius, ", is:", area)

#3. Write a program that allows a user to enter his or her two favorite foods. 
#   The program should then print out the name of a new food by joining the original food names together.
favOne = input("What is your favorite food?\n")
favTwo = input("What is your second favorite food?\n")
print("You should try", favOne + favTwo)

#4. Write a Tipper program where the user enters a restaurant bill total. 
#   The program should then display two amounts: a 15 percent tip and a 20 percent tip.
billTotal = float(input("Please enter bill total "))
print("15% tip =", billTotal * .15)
print("20% tip =", billTotal * .2)

#5. Write a Car Salesman program where the user enters the base price of a car. 
#   The program should add on a bunch of extra fees such as tax, license, dealer prep, and destination charge. 
#   Make tax and license a percent of the base price. The other fees should be set values. Display the actual price of the car once all the extras are applied.
carPrice = float(input("Enter car price: "))
tax = carPrice * .07
license = 145
dealerPrep = carPrice * .03
destination = 250
carPrice += tax + license + dealerPrep + destination
print("Total price after fees and taxes:", carPrice)

#6. Let the variable x be "dog" and the variable y be "cat". Write the values returned by the following operations:
#   a. x + y
##Answer: dogcat
#   b. "the " + x + " chases the " + y
##Answer: the dog chases the cat
#   c. x * 4
##Answer: dogdogdogdog

#7. Assume that the variable x has the values 55. Use an assignment statement to increment the value of x by 1.
x = 55
x = x + 1