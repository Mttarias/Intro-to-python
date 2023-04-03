# Midterm Exam - Answer the following three questions within 40 minutes


# 1. Create a loop to ask the user for input. The input should be an integer.
# Take the number from the input and add any integers that came before it, all the way to 0
# Ex. If you choose 5 as input, the loop should add 5, 4, 3, 2, 1, and 0 together.
# 5 points

# Enter your code here:
userInput = int(input("Please enter an integer: "))
sum = 0

for x in range(userInput, -1, -1):
    sum += x
print(sum)

# 2. Create a program that allows you to add items to a list and recall its contents
# The recall of the list should print the items individually, without any
# additional marks (hint: do not just print the list)
#15 points

# Enter your code here:
finalList = []

while True:
    add = input("Enter item to add to list(if done press enter): ")

    if add == "":
        break
    
    finalList.append(add)

for item in finalList:
    print(item, end=" ")
print()

# 3. Create a menu using if, elif, else statements.
# The menu should have four options:
# Option 1 should add two numbers, inputs from the user
# Option 2 should get the square of one number, user input
# Option 3 should give a famous quote at random (3+ quotes)
# Option 4 should exit the program
# Anything else is up to you.
#20 points

# Enter your code here:
import random

quotes = ("\"The future belongs to those who prepare for it today.\" -Malcolm X", "\"I have no special talent. I am only passionately curious.\" -Albert Einstein"
          , "\"Those who dare to fail miserably can achieve greatly.\" -John F. Kennedy", "\"Wisely, and slow. They stumble that run fast.\" -William Shakespeare"
          , "\"The Last Argument of Kings.\" -as inscribed on the cannons of King Louis XVII")

while True:
    print("1. Add two integers together\n2. find the square of one number\n3. Display famous quote\n4. Exit")
    menu = int(input("Please choose an option: "))
    
    if menu == 1:

        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))

        print(number1 + number2)
    
    elif menu == 2:

        numberSquare = int(input("Enter the number you wish to find the square of: "))
        
        print(numberSquare * numberSquare)

    elif menu == 3:

        print(random.choice(quotes))

    elif menu == 4:

        print("exiting")
        break

    else:
        print("Not a valid choice.")