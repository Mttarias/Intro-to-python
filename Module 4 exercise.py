#1 What is a variable?
# A variable is a named attribute with an assigned value.

#2 What is a constant?
# A constant is a variable whose value is not meant to changed.

#3 Can a variable be changed once assigned?
# yes it can.

#4 Write a program that counts for the user. Let the user enter the starting number, the ending number, and the amount by which to count.
start = int(input("Please enter the starting number: "))
end = int(input("Please enter the ending number: "))
step = int(input("Please enter the amount by which to count: "))

for x in range(start, end+step, step):
    if x <= end:
        print(x)

#5 Create a program that gets a message from the user and then prints it out backwards.
message = input("Please enter a message: ")
backwardsCount = len(message)
reverseMessage = ""
for y in range(backwardsCount, 0, -1):
    reverseMessage += message[y-1]
print(reverseMessage)
#6 Create a game where the computer picks a random word and the player has to guess that word. The computer tells the player how many letters are in the word.
#  Then the player gets five chances to ask if a letter is in the word. The computer can only respond with “yes” or “no”. Then, the player must guess the word.
import random

WORDS = ("Cloud", "Code", "Harvest", "Books", "Monty", "Sword")
word = random.choice(WORDS)
count = 0

print("There are", len(word), "letters in the word.")

while count < 5:
    letter = input("Please enter a letter to check if it is present in the word: ")
    if letter.lower() in word.lower():
        print("yes")
    else:
        print("no")
    count += 1

guess = input("Please enter your guess: ")

if guess.lower() == word.lower():
    print("Correct! Congratulations")
else:
    print("Incorrect, better luck next time")
print("The end..?")