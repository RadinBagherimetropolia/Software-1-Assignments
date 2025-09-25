import math
#input
first = int(input("Enter the diameter of a round pizza in centimeters: "))
second = int(input("Enter the price of the pizza in euros: "))
third = int(input("Enter the diameter of a second round pizza in centimeters: "))
fourth = int(input("Enter the price of the second pizza in euros: "))
#def
def pizza(x1,x2):
    s = ((x1 / 200)**2)*math.pi
    result = x2/s
    return result
a = pizza(first,second)
b = pizza(third,fourth)
print(f"the price of the first pizza per meter is {a:.3f}\nthe price of the second pizza per meter is {b:.3f}")
if a>b:
    print("second pizza has a lower unit price")
else:
    print("first pizza has a lower unit price")


