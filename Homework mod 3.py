import random
#1 What is the code that comes after an if statement called?
# block

#2 You need to test a condition then execute one set of statements if the condition is true. 
#  If the condition is false, you need to execute a different set of statements. What structure will you use?
# if else structure

#3 What is an infinite loop? Write the code for an infinite loop
#  Loop that doesnt have a break and will keep going without end.
#while True:
 #   print("the beginning of the end is")

#4 Write a program that simulates a fortune cookie.
#  The program should display one of five unique fortunes, at random, each time it’s run.
#fortunes = ["Try again later", "Your future looks bright", "Love is inside you" 
#            , "Doing something is half the battle the other half is finishing", "Chaos is a ladder"]
#print(random.choice(fortunes))
fortune = random.randrange(5) + 1

if fortune == 1:
    print("Try again later")
elif fortune == 2:
    print("Your future looks bright")
elif fortune == 3:
    print("Love is inside you")
elif fortune == 4:
    print("Doing something is half the battle the other half is finishing")
elif fortune == 5:
    print("Chaos is a ladder")

#5 Write a program that flips a coin 100 times and then tells you the number of heads and tails.
count = 0
heads = 0
tails = 0

while count < 100:
    if random.randrange(2) == 0:
        heads += 1
    else:
        tails += 1
    count += 1

print("total number of heads:", heads, "\ntotal number of tails:", tails)
