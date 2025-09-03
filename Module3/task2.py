user = input(" enter the cabin class: ").lower()
if user == "lux":
    print("upper-deck cabin with a balcony.")
elif user == "a":
    print("above the car deck, equipped with a window.")
elif user == "b":
    print("windowless cabin above the car deck.")
elif user == "c":
    print("windowless cabin below the car deck.")
else:
    print("invalid cabin class")


