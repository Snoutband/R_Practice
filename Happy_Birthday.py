from datetime import datetime
datemonth = datetime.today().month
dateday = datetime.today().day
decision = input("Check?, Yes or No ")
if decision == "Yes":
    I = input("Enter your intitals ")
    Ilist = ['TS']
    if I in Ilist:
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
    else:
        name = I
        print("Not for you", name)
