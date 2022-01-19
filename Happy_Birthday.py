from datetime import datetime
datemonth = datetime.today().month
dateday = datetime.today().day
message = "It is your birthday!"
test_decision = ['yes',"Yes",'y',"Y"]
decision = input("Check?, Yes or No ")
if decision in test_decision:
    I = input("Enter your intitals ")
    Ilist = ['TS', 'ts']
    if I in Ilist:
        if datemonth == 1 and dateday == 26:
            print(message)
        elif datemonth == 1:
                print("Birthday Month!")
        elif datemonth == 12:
                print("One Month away!")
        else:
            print("Better luck next time")
    if I not in Ilist:
            new_message = message.replace("It is your birthday!","NOT for you!")
            print(new_message)
else:
    print (':(')
