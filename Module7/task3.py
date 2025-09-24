#creating dictionary
airports = {"EFHK":"Helsinki-Vantaa Airport",
            "OSL":"Oslo Airport",
            "FCO":"Rome Airport",
            "SVO":"Moscow Airport",
            "DUB":"Dublin Airport",
            "ZRH":"Zürich Airport",
            "YYZ":"Toronto Airport",}
#while loop
while True:
    user = input("a)enter a new airport\n b)fetch the information of an existing airport\n c)quit\n ")
    if user == "a":
        x = input("enter the ICAO code of the airport ").upper()
        y = input("enter the name name of the airport ")
        airports[x] = y
    elif user == "b":
        z = input("enter the ICAO code of the airport ").upper()
        print(airports[z])
    else:
        break

