#set
names = set()
while True:
    user = input("Enter the name or exit with space: ")
    if user in names:
        print("Existing name")
    else:
        if user == "":
            break
        else:
           print("New name")
           names.add(user)
for i in names:
    print(i)