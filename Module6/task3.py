#def
def convert(fuel):
    result = fuel * 3.785411784
    return result
#main

while True:
    user = int(input("Enter gasoline volume in American gallons: "))
    if 0<=user:
        print(convert(user))
    else:
        print("wrong volume")
        break


