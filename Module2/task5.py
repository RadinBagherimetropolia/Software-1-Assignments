talents = int(input("Enter talents: "))
pounds = int(input("Enter ponds: "))
lots = float(input("Enter  lots: "))
first_number = talents * 20 * 32 * 13.3
second_number = pounds * 32 * 13.3
third_number = lots * 13.3
result = first_number + second_number + third_number
kilograms = result/1000
grams = result%1000
print(f"your mass in modern units is : {kilograms:6.1f}kilograms and {grams:6.2f}grams")
