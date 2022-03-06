
#BMI Calculator
_mass =input("Your Mass/Weight  in kg:")
_height =input("Your Height in m : ")
BMI:float
BMI = int(_mass)/(float(_height)*float(_height))

print(f"BMI : {round(BMI)}")
if BMI<18:
    print("You are under weight")
elif BMI>18:
    print("You are over weight")
else:
    print("cooooooooool! Perfect Balance")
    
# income =12_000_000
# print(income)
# from xmlrpc.client import Boolean

# from numpy import char


# from tokenize import String


# isAlive:bool
# age:int
# BloodGroup:String

# in_= input("Are you Alive right now or not ????")

# if in_ =="yes":
#     isAlive =True
# else:
#     isAlive=False

# print(f"So you are alive =={isAlive}")

# name =input("What's Your Name : ")
# print(f"Your Name {name} has {len(name)} characters.")

# print("something --->>>"+str(5))

