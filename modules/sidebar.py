import streamlit as st

from modules.data import get_data

features_dict = {
    "Age": {"variable": "age", "input_type": "number_input"},
    "Gender": {
        "variable": "gender",
        "input_type": "selectbox",
        "options": {1: "Female", 2: "Male"},
    },
    "Height": {"variable": "height", "input_type": "number_input"},
    "Weight": {"variable": "weight", "input_type": "number_input"},
    "Systolic blood pressure": {"variable": "ap_hi", "input_type": "number_input"},
    "Diastolic blood pressure": {"variable": "ap_lo", "input_type": "number_input"},
    "Cholesterol": {
        "variable": "cholesterol",
        "input_type": "selectbox",
        "options": {1: "Normal", 2: "Above Normal", 3: "Well Above Normal"},
    },
    "Glucose": {
        "variable": "gluc",
        "input_type": "selectbox",
        "options": {1: "Normal", 2: "Above Normal", 3: "Well Above Normal"},
    },
    "Smoking": {
        "variable": "smoke",
        "input_type": "radio",
        "options": {0: "No", 1: "Yes"},
    },
    "Alcohol intake": {
        "variable": "alco",
        "input_type": "radio",
        "options": {0: "No", 1: "Yes"},
    },
    "Physical activity": {
        "variable": "active",
        "input_type": "radio",
        "options": {0: "No", 1: "Yes"},
    },
}


def create_input(sb, input_dict, label, key, values):
    if key["input_type"] == "number_input":
        input_dict[key["variable"]] = sb.number_input(
            label, 0, int(values.max() * 2), int(values.mean())
        )
    elif key["input_type"] == "radio":
        input_dict[key["variable"]] = sb.radio(
            label, options=key["options"], format_func=lambda x: key["options"][x]
        )
    elif key["input_type"] == "selectbox":
        input_dict[key["variable"]] = sb.selectbox(
            label, options=key["options"], format_func=lambda x: key["options"][x]
        )


def sidebar():
    sb = st.sidebar
    sb.image("assets/heart_logo.png", width=150)

    input_dict = {}

    data = get_data()

    for label, key in features_dict.items():
        values = data[key["variable"]]
        create_input(sb, input_dict, label, key, values)

    return input_dict
