#life remaining ...
#2022


age:int
years_remaining:int
months_remaining:int
days_remaining:int
weeks_remaining:int

age =int(input("please enter your age :"))
print(f"Your current age : {age}")

years_remaining=100-age
days_remaining=years_remaining*365
weeks_remaining=years_remaining*52
months_remaining=years_remaining*12


print(f"days left : {days_remaining}\nweeks left : {weeks_remaining}\nMonths remaining : {months_remaining}\nyears left : {years_remaining}\n")

