import tkinter as tk
from tkinter import messagebox
def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())

        if height <= 0 or weight <= 0:
            raise ValueError

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi} ({category})")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for height and weight.")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")
root.resizable(False, False)

# Labels and entry fields
tk.Label(root, text="Enter Height (m):").pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack(pady=5)

tk.Label(root, text="Enter Weight (kg):").pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
