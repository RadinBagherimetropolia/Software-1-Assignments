num_list = []
while True:
    user = input("Enter a number or exit with leaving a blank space : ")
    if user == "":
        break
    number = int(user)
    num_list.append(number)
num_list.sort(reverse=True)
for n in num_list[0:5]:
    print(n)
