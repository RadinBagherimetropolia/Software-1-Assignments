import random
#input
first =int(input("Enter sides: "))
#def function
def dice(sides):
    sides = random.randint(1, sides)
    return sides
while True:
    user_sides = dice(first)
    if user_sides == first:
        print(f"good job\n the result was {user_sides}!")
        break
    else:
        print(f"the result was {user_sides}")
