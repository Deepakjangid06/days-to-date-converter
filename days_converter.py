days = int(input("enter days : "))

#for calculate the years, 1 year = 365 days
year = days//365
remaining_days = days%365

#for calculate the months, 1 month = 30 days
month = remaining_days//30
remaining_days = remaining_days%30

#for calculate the weeks, 1 week = 7 days
week = remaining_days//7

#for calculate the days
remaining_days = remaining_days%7

#now, we print all the values or outputs
print("years : ", year)
print("months : ", month)
print("weeks : ", week)
print("days : ", remaining_days)
