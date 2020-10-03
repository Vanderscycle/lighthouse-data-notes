import time

# name is a variable. It contains a string
name = "Thomas"
print("Hello " + name + ", it's very nice to meet you!")

# taxRate, subtotal, tax and total are all variables that contain numbers
taxRate = 0.14
subtotal = 20
tax = subtotal * taxRate
total = subtotal + tax
print("Your total bill is: ")
print(total)

# travelDestinations is a variable containing a list
# city is a variable - its value is changing a few times
travelDestinations = ["Vancouver","Montreal","Calgary","Toronto"]
for city in travelDestinations:
    print(city + " looks like a cool place to go!!")
    
def nani():
    name = input("What is your character's name: ")
    print("Anime Mega Chad: Omae Wa Mou Shindeiru ")
    time.sleep(.5)
    print(f"{name}: Nani!!!")
    return

#nani()

name = input("CONTESTANT! Please enter your name:")
print(f"CONTESTANT {name} remember that formated strings are so satisfying")