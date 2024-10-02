def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    if unit.lower() == 'celsius':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        print(f"{value}°C is equal to {fahrenheit:.2f}°F and {kelvin:.2f}K.")
    elif unit.lower() == 'fahrenheit':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        print(f"{value}°F is equal to {celsius:.2f}°C and {kelvin:.2f}K.")
    elif unit.lower() == 'kelvin':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        print(f"{value}K is equal to {celsius:.2f}°C and {fahrenheit:.2f}°F.")
    else:
        print("Invalid unit. Please choose from Celsius, Fahrenheit, or Kelvin.")

temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit of the temperature (Celsius, Fahrenheit, Kelvin): ")
convert_temperature(temperature, unit)
