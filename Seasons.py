monthLengths = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30,
                "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

fullMonthSeason = {"January": "Winter", "February": "Winter", "April": "Spring", "May": "Spring",
                    "July": "Summer", "August": "Summer", "October": "Autumn", "November": "Autumn"}

def calculateSeason(month, day):
    if month in fullMonthSeason:
        print(fullMonthSeason[month])
    elif month == "March" and day <= 19:
        print("Winter")
    elif month == "March" and day > 19:
        print("Spring")
    elif month == "June" and day <= 20:
        print("Spring")
    elif month == "June" and day > 20:
        print("Summer")
    elif month == "September" and day <= 21:
        print("Summer")
    elif month == "September" and day > 21:
        print("Autumn")
    elif month == "December" and day <= 20:
        print("Autumn")
    elif month == "December" and day > 20:
        print("Winter")


def validateInput():
    month = input("Please enter a month of the year: ")
    month = month.lower().capitalize()
    try:
        day = int(input("Please enter a day: "))
    except ValueError:
        print("Invalid")
    
    if month in monthLengths:
        if day <= monthLengths[month] and day > 0:
            calculateSeason(month, day)
        else:
            print("Invalid")
    else:
        print("Invalid")


print("This program takes a month and day and outputs the season")
validateInput()