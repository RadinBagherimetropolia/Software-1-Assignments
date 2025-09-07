correct_username = "python"
correct_password = "rules"
max_attempts = 5
attempts = 0
while attempts < max_attempts:
    username = input("enter a username: ")
    password = input("enter a password: ")
    attempts = attempts + 1
    if username == correct_username and password == correct_password:
        print("welcome")
        break
    else:
        if attempts < max_attempts:
            print("enter the username and password again")
        else:
            print("access denied")