import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Insect_Species_Dataset.csv")

X = df.drop("Species", axis=1)
y = df["Species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nINSECT SPECIES CLASSIFICATION RESULTS")
print("--------------------------------------")
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))
print("Model Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

cm = confusion_matrix(y_test, predictions)

plt.figure(figsize=(9, 6))
sns.heatmap(
    cm, annot=True, fmt="d", cmap="YlGnBu",
    xticklabels=model.classes_,
    yticklabels=model.classes_
)
plt.title("Insect Species Classification - Confusion Matrix")
plt.xlabel("Predicted Species")
plt.ylabel("Actual Species")
plt.tight_layout()
plt.savefig("Insect_Classification_Confusion_Matrix.png", dpi=300)
plt.show()

importance = pd.Series(
    model.feature_importances_, index=X.columns
).sort_values()

importance.plot(kind="barh", figsize=(8, 5))
plt.title("Feature Importance in Insect Classification")
plt.xlabel("Importance")
plt.tight_layout()
plt.savefig("Insect_Feature_Importance.png", dpi=300)
plt.show()

import joblib
joblib.dump(model, "Insect_Species_Model.pkl")

print("\nModel and graphs saved successfully!")
