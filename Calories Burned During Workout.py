#The following equation estimates the average calories burned for a person when exercising, which is based on a scientific journal article (source

#Links to an external site.):

#calories = ( (Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991 ) x Time / 8.368

#Write a program using inputs age (years), weight (pounds), heart rate (beats per minute), and time (minutes), respectively. Output the average calories burned for a person.

#Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
#print(f'Calories: {calories:.2f} calories')
age = int(input("please enter your age: "))

weight = float(input("Please enter your weight(lbs): "))

heartRate = int(input("Please enter your heart rate(bpm): "))

time = float(input("enter your workout time in minutes: "))

calories = (((age * 0.2757) + (weight * 0.03295) + (heartRate * 1.0781) - 75.4991) * time / 8.368)

print(f'Calories: {calories:.2f} calories')
