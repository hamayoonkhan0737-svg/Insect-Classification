import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib
import os

model = joblib.load(os.path.join(os.path.expanduser("~"), "Insect_Species_Model.pkl"))

species_info = {
    "Whitefly": "A sap-sucking insect pest that damages crops.",
    "Grasshopper": "A chewing insect that feeds on leaves and shoots.",
    "Fruit Fly": "A pest that damages fruits during development.",
    "Cotton Bollworm": "A major cotton pest that damages squares and bolls.",
    "Aphid": "A small sap-sucking insect that can transmit plant viruses.",
    "Ladybird Beetle": "A beneficial insect that feeds on aphids and other pests."
}

root = tk.Tk()
root.title("Insect Species Classification System")
root.geometry("550x680")
root.configure(bg="#eaf2f8")
root.resizable(False, False)

tk.Label(
    root, text="INSECT SPECIES CLASSIFIER",
    font=("Arial", 19, "bold"),
    bg="#eaf2f8", fg="#154360"
).pack(pady=20)

fields = [
    "Body Length (mm)",
    "Body Width (mm)",
    "Wing Length (mm)",
    "Antenna Length (mm)",
    "Leg Length (mm)"
]

columns = [
    "Body_Length_mm",
    "Body_Width_mm",
    "Wing_Length_mm",
    "Antenna_Length_mm",
    "Leg_Length_mm"
]

entries = []

for field in fields:
    tk.Label(root, text=field, font=("Arial", 11),
             bg="#eaf2f8").pack(pady=3)

    entry = tk.Entry(root, font=("Arial", 12), justify="center")
    entry.pack()
    entries.append(entry)

result_label = tk.Label(
    root, text="Prediction will appear here",
    font=("Arial", 14, "bold"),
    bg="#eaf2f8", fg="#34495e",
    wraplength=480
)
result_label.pack(pady=18)

confidence_label = tk.Label(
    root, text="",
    font=("Arial", 12, "bold"),
    bg="#eaf2f8", fg="#117864"
)
confidence_label.pack(pady=5)

info_label = tk.Label(
    root, text="",
    font=("Arial", 11),
    bg="#eaf2f8", fg="#34495e",
    wraplength=450
)
info_label.pack(pady=10)

def predict():
    try:
        values = [float(entry.get()) for entry in entries]

        data = pd.DataFrame([values], columns=columns)

        probabilities = model.predict_proba(data)[0]
        prediction_index = probabilities.argmax()

        species = model.classes_[prediction_index]
        confidence = probabilities[prediction_index] * 100

        result_label.config(
            text="Predicted Species: " + species,
            fg="#117864"
        )

        confidence_label.config(
            text=f"Prediction Confidence: {confidence:.2f}%"
        )

        info_label.config(
            text="Species Information: " + species_info.get(species, "Information unavailable.")
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def clear():
    for entry in entries:
        entry.delete(0, tk.END)

    result_label.config(text="Prediction will appear here", fg="#34495e")
    confidence_label.config(text="")
    info_label.config(text="")

tk.Button(
    root, text="PREDICT SPECIES",
    command=predict,
    font=("Arial", 12, "bold"),
    bg="#2874a6", fg="white",
    width=22, height=2
).pack(pady=12)

tk.Button(
    root, text="CLEAR",
    command=clear,
    font=("Arial", 11, "bold"),
    bg="#c0392b", fg="white",
    width=15
).pack(pady=5)

tk.Label(
    root, text="Agricultural Entomology | Machine Learning",
    font=("Arial", 9), bg="#eaf2f8", fg="gray"
).pack(side="bottom", pady=15)

root.mainloop()
