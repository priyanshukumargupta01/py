# Write a Python program to convert temperatures to and from Celsius, Fahrenheit.  

temp = float(input("Enter temperature: "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()

if unit == "C":
    fahrenheit = (temp * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

elif unit == "F":
    celsius = (temp - 32) * 5 / 9
    print("Temperature in Celsius:", celsius)

else:
    print("Invalid unit. Please enter C or F.")