﻿# Heart Disease Predictor

![Website](https://github.com/christianduhp/heart_disease_predictor/assets/85292359/824a574a-c2e3-4532-be29-e69381e8593c)


## Overview

This Streamlit application predicts the presence or absence of cardiovascular disease using machine learning techniques. It visualizes input data, provides predictions, and performs exploratory data analysis. The radar chart provides a visual representation of the patient's health profile, while the predictions help in understanding the likelihood of cardiovascular disease. 


## Features

- **Radar Chart**: Visualizes the health profile based on age, height, weight, and blood pressure.
- **Prediction**: Predicts cardiovascular disease based on input parameters.
- **Exploratory Data Analysis**: Displays SHAP force plots and distribution charts for numerical and categorical features.

## Machine Learning Details

### Dataset

The dataset used for training and prediction is sourced from `model/cardio_train.csv`.

### Features

| Feature                                       | Variable Type       | Variable    | Value Type                                       |
|-----------------------------------------------|---------------------|-------------|--------------------------------------------------|
| Age                                           | Objective Feature   | age         | int (days)                                       |
| Height                                        | Objective Feature   | height      | int (cm)                                         |
| Weight                                        | Objective Feature   | weight      | float (kg)                                       |
| Gender                                        | Objective Feature   | gender      | categorical code - 1: female, 2: male            |
| Systolic blood pressure                       | Examination Feature | ap_hi       | int                                              |
| Diastolic blood pressure                      | Examination Feature | ap_lo       | int                                              |
| Cholesterol                                   | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |
| Glucose                                       | Examination Feature | gluc        | 1: normal, 2: above normal, 3: well above normal |
| Smoking                                       | Subjective Feature  | smoke       | binary                                           |
| Alcohol intake                                | Subjective Feature  | alco        | binary                                           |
| Physical activity                             | Subjective Feature  | active      | binary                                           |
| Presence or absence of cardiovascular disease | Target Variable     | cardio      | binary                                           |


## Setup

To run the application locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/christianduhp/heart-disease-predictor.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   streamlit run app.py
   ```

## Notes

- Ensure Python 3.x is installed.
- The application uses Streamlit for the web interface and Plotly for interactive visualizations.
