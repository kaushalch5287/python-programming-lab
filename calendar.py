date = eval(input("enter date: "))
month = eval(input("enter month number in format(1,2,3...): "))

if month == 1:
    cal = 365 - date 
    print("no. of days left in the year 2019: ",cal)
elif month == 2:
    cal = 365 - date - 31
    print("no. of days left in the year 2019: ",cal)
elif month == 3:
    cal = 365 - date - 59
    print("no. of days left in the year 2019: ",cal)
elif month == 4:
    cal = 365 - date - 90
    print("no. of days left in the year 2019: ",cal)
elif month == 5:
    cal = 365 - date - 120
    print("no. of days left in the year 2019: ",cal)
elif month == 6:
    cal = 365 - date - 151
    print("no. of days left in the year 2019: ",cal)
elif month == 7:
    cal = 365 - date - 181
    print("no. of days left in the year 2019: ",cal)
elif month == 8:
    cal = 365 - date - 212
    print("no. of days left in the year 2019: ",cal)
elif month == 9:
    cal = 365 - date - 243
    print("no. of days left in the year 2019: ",cal)
elif month == 10:
    cal = 365 - date - 273
    print("no. of days left in the year 2019: ",cal)
elif month == 11:
    cal = 365 - date - 304
    print("no. of days left in the year 2019: ",cal)
elif month == 12:
    cal = 365 - date - 334
    print("no. of days left in the year 2019: ",cal)
else:
    print("invalid format entered")
