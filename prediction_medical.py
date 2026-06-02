import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Dataset
data = {
    "Age": [25,45,35,50,60,30,55,40,65,28,48,52,38,70,33,41,57,29,62,36],
    "BloodPressure": [120,140,130,150,160,125,155,135,170,118,145,152,128,175,122,138,158,121,168,132],
    "Cholesterol": [180,240,200,260,280,190,270,220,300,175,250,265,195,310,185,230,275,182,295,205],
    "Disease": [0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,1,0,1,0]
}

df = pd.DataFrame(data)

X = df[["Age", "BloodPressure", "Cholesterol"]]
y = df["Disease"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


def predict_disease():
    try:
        age = int(age_entry.get())
        bp = int(bp_entry.get())
        chol = int(chol_entry.get())

        prediction = model.predict([[age, bp, chol]])[0]
        probability = model.predict_proba([[age, bp, chol]])[0][1]

        risk = probability * 100

        if prediction == 1:
            result_label.config(
                text=f"⚠ Disease Risk Detected\nRisk: {risk:.2f}%",
                fg="red"
            )
        else:
            result_label.config(
                text=f"✓ No Disease Risk\nRisk: {risk:.2f}%",
                fg="green"
            )

    except:
        messagebox.showerror("Error", "Please enter valid numbers")


# GUI Window
root = tk.Tk()
root.title("Disease Prediction System")
root.geometry("500x450")

title = tk.Label(
    root,
    text="Disease Prediction System",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

tk.Label(root, text="Blood Pressure").pack()
bp_entry = tk.Entry(root)
bp_entry.pack(pady=5)

tk.Label(root, text="Cholesterol").pack()
chol_entry = tk.Entry(root)
chol_entry.pack(pady=5)

predict_btn = tk.Button(
    root,
    text="Predict",
    command=predict_disease,
    font=("Arial", 12)
)
predict_btn.pack(pady=15)

result_label = tk.Label(
    root,
    text="Enter values and click Predict",
    font=("Arial", 14)
)
result_label.pack(pady=20)

root.mainloop()
