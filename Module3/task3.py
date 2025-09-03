user_gender = input("what is your gender?: ").lower()
user = float(input("enter your hemoglobin value(g/l): "))
if user_gender == "male":
    if user < 134:
        print("your hemoglobin value is low")
    if user > 167:
        print("your hemoglobin value is high")
    if 134 <= user <= 167:
      print("your hemoglobin value is normal")
if user_gender == "female":
    if user  < 117:
        print("your hemoglobin value is low")
    if user > 155:
        print("your hemoglobin value is high")
    if 117 <= user <= 155:
        print("your hemoglobin value is normal")


