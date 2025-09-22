import random
dice_user = int(input("enter the number of dice that you want to roll: "))
total = 0
for n in range(dice_user):
    dice = random.randint(1, 6)
    total += dice
print(f"the sum of the dices is: {total}")
