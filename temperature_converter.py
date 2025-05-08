def convert_temperature():
    try:
        temp = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

        if unit == "C":
            result = (temp * 9/5) + 32
            print(f"{temp}°C is {result:.2f}°F")
        elif unit == "F":
            result = (temp - 32) * 5/9
            print(f"{temp}°F is {result:.2f}°C")
        else:
            print("Invalid unit! Please enter C or F.")

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    convert_temperature()
