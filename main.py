def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32

def main():
    print("=== Temperature Conversion Program ===")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    try:
        value = float(input("Enter temperature value: "))
        unit = input("Enter original unit (C/F/K): ").strip().upper()
        if unit == "C":
            print(f"Fahrenheit: {celsius_to_fahrenheit(value):.2f} °F")
            print(f"Kelvin: {celsius_to_kelvin(value):.2f} K")
        elif unit == "F":
            print(f"Celsius: {fahrenheit_to_celsius(value):.2f} °C")
            print(f"Kelvin: {fahrenheit_to_kelvin(value):.2f} K")
        elif unit == "K":
            if value < 0:
                print("Kelvin temperature cannot be below 0.")
                return
            print(f"Celsius: {kelvin_to_celsius(value):.2f} °C")
            print(f"Fahrenheit: {kelvin_to_fahrenheit(value):.2f} °F")
        else:
            print("Invalid unit. Please use C, F, or K.")
    except ValueError:
        print("Please enter a valid numeric temperature.")

if __name__ == "__main__":
    main()
