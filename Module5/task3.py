#create input
number = int(input("Enter a number: "))
#create for loop
if 0 < number <= 1:
    print(f"{number} is not a prime number ")
else:
    for numbers in range(2, number):
      if number % numbers == 0:
        print(f"{number} is not a prime number")
        break
    else:
        print(f"{number} is a prime number")





