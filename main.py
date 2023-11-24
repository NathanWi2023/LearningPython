import datetime as dt

userinput = input("Enter your date of birth (DD/MM/YYYY)")

day , month, year = userinput.split("/")
print (f"Day: {day}, Month: {month}, Year: {year}")

dayborn = int(day)
monthborn = int(month)
yearborn= int(year)

yearnow = dt.datetime.now().year
monthnow = dt.datetime.now().month
daynow = dt.datetime.now().day

hashadbirthday = monthnow > monthborn or (monthnow == monthborn and daynow >= dayborn)

if hashadbirthday:
    age = yearnow - yearborn
else:
    age = yearnow - yearborn - 1

print(f"You are {age} years old.")