#right a function
import random
def dice():
    dice_1 = random.randint(1, 6)
    return dice_1
while True:
    result = dice()
    if result == 6:
        print(f"finally the result was {result}!\n good job")
        break
    else:
        print(f"the result was {result}")

