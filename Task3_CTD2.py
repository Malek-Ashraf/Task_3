####----------Challenge 2----------#####
print("Choose a conversion:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter 1 or 2: ")
if choice == '1':
    TemperatureC = float(input("Enter the temperature in Celsius: "))   
    Fahrenheit = (TemperatureC * 9/5) + 32
    print("Temperature in Fahrenheit: ", Fahrenheit)
elif choice == '2':
    Fahrenheit = float(input("Enter the temperature in Fahrenheit: "))   
    Celsius = (Fahrenheit - 32) * 5/9
    print("Temperature in Celsius: ", Celsius)
else:
    print("Invalid choice. Please enter 1 or 2.")