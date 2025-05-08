def calculate_simple_interest():
    try:
        principal = float(input("Enter the Principal amount: "))
        rate = float(input("Enter the Rate of interest (%): "))
        time = float(input("Enter the Time (in years): "))

        simple_interest = (principal * rate * time) / 100
        print(f"Simple Interest = {simple_interest}")
    except ValueError:
        print("Please enter valid numeric values!")

if __name__ == "__main__":
    calculate_simple_interest()
