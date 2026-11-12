import pandas as pd
import numpy as np

np.random.seed(42)

species_data = {
    "Cotton Bollworm": [18, 5, 12, 4, 3],
    "Whitefly": [2, 1, 3, 2, 2],
    "Aphid": [3, 2, 1, 1, 1],
    "Ladybird Beetle": [7, 5, 4, 3, 5],
    "Grasshopper": [35, 8, 25, 10, 6],
    "Fruit Fly": [5, 3, 6, 4, 2]
}

records = []

for species, means in species_data.items():
    for i in range(100):
        body_length = np.random.normal(means[0], means[0]*0.12)
        body_width = np.random.normal(means[1], means[1]*0.12)
        wing_length = np.random.normal(means[2], means[2]*0.12)
        antenna_length = np.random.normal(means[3], means[3]*0.12)
        leg_length = np.random.normal(means[4], means[4]*0.12)

        records.append([
            max(body_length, 0.1),
            max(body_width, 0.1),
            max(wing_length, 0.1),
            max(antenna_length, 0.1),
            max(leg_length, 0.1),
            species
        ])

df = pd.DataFrame(records, columns=[
    "Body_Length_mm",
    "Body_Width_mm",
    "Wing_Length_mm",
    "Antenna_Length_mm",
    "Leg_Length_mm",
    "Species"
])

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

df.to_csv("Insect_Species_Dataset.csv", index=False)

print("DATASET CREATED SUCCESSFULLY!")
print("Total Samples:", len(df))
print("\nSpecies Distribution:")
print(df["Species"].value_counts())
print("\nFirst 5 Records:")
print(df.head())
