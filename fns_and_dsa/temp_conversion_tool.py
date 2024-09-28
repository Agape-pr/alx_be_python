# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this in Celsius or Fahrenheit? (C/F): ")

if unit == "C":
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temp:.2f}°F.")
elif unit == "F":
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temp:.2f}°C.")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
