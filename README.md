# 🐛 Insect Species Classification Using Machine Learning

## Project Overview
This project focuses on developing a Python-based machine learning application for classifying six insect species using morphological measurements.

The system uses a Random Forest Classifier to predict insect species based on five body measurements.

## Insect Species
The model classifies the following six species:

1. Whitefly
2. Grasshopper
3. Fruit Fly
4. Cotton Bollworm
5. Aphid
6. Ladybird Beetle

## Dataset Description
- Total samples: 600
- Number of species: 6
- Samples per species: 100
- Dataset type: Synthetic (simulated)

### Input Features
- Body Length (mm)
- Body Width (mm)
- Wing Length (mm)
- Antenna Length (mm)
- Leg Length (mm)

## Machine Learning Algorithm
Random Forest Classifier (Scikit-learn).

## Model Performance
- Training samples: 480
- Testing samples: 120
- Test accuracy: 100%

**Note:** The reported accuracy was obtained using a synthetic dataset. It does not represent validated real-world insect identification accuracy.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Tkinter
- Joblib

## Application Features
- Insect species prediction
- Prediction confidence percentage
- Species information
- Graphical user interface (GUI)
- Standalone Windows executable

## Project Files
- `Insect_GUI.py` – Desktop application
- `Train_Insect_Model.py` – Model training
- `Insect_Species_Dataset.py` – Dataset generation
- `Insect_Species_Dataset.csv` – Synthetic dataset
- `Insect_Species_Model.pkl` – Trained model

## Research Limitation
The current model was developed using simulated morphological measurements. Further research using actual insect specimens and independently collected field data is required to evaluate its real-world performance.

## Author
Agricultural Entomology | Machine Learning Project
