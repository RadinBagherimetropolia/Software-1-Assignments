#create input
user = input("Enter a city? ")
#create list
city = []
city.append(user)
len(city)
#for loop
for i in city:
    if len(city)<5:
        user = input("Enter a city? ")
        city.append(user)
    elif i==5:
        break

for n in city:
    print(n)


