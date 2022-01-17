from datetime import datetime
datemonth = datetime.today().month
dateday = datetime.today().day
for i in range(1):
    if datemonth == 1 and dateday == 26:
        print("It is your birthday!")
        for x in range("Happy Birthday!"):
            print(x)
    elif datemonth == 1:
        print("Birthday Month!")
    elif datemonth == 12:
        print("One Month away!")
    else:
        print("Better luck next time")
print()
