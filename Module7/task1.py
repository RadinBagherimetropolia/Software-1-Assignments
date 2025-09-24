#tuple
seasons = ("winter", "spring", "summer", "autumn")
#input
user  = int(input("Enter the number of the month (1-12): "))
if user <= 2 or user == 12:
    print(seasons[0])
elif 3 <= user <= 5:
    print(seasons[1])
elif 6 <= user <= 8:
    print(seasons[2])
else:
    print(seasons[3])



