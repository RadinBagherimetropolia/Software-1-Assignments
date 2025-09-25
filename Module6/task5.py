#creating lists
list_1 = []
list_2 = []
#def
def math(new):
    for i in new:
        if i % 2 == 0:
            list_2.append(i)


    return(list_2)

#while loop
while True:
    user =input('Enter a number: ')
    if user =="":
        break

    else:
        num = float(user)
        list_1.append(num)
math(list_1)
print(list_2)





