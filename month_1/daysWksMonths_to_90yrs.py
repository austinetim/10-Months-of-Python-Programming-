#365 days, 52 weeks, 12 months

age =  int(input("Enter your age: "))

days_in_90 = 365*90

weeks_in_90 = 52*90

months_in_90 = 12*90

days_left = days_in_90 - age*365
weeks_left = weeks_in_90 - age*52
months_left = months_in_90 - age*12
message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left to age 90"

print(message)