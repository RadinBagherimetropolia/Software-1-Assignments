#def
def plus(number):
    result = sum(number)
    return result
#create list
num = []
#main
while True:
    user =input("Enter the number or get the sum with space: ")
    if user =="":
        break
    else:
        x = float(user)
        num.append(x)
plus(num)
print(plus(num))