numbers = []
while True:
    user = (input("Enter a number: "))
    if user == "":
        break
    number = float(user)
    numbers.append(user)
    numbers.sort()
small = min(numbers)
large = max(numbers)
print(f"The smallest number is: {small} and the largest number is: {large}")