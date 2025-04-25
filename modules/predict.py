import pickle
import pandas as pd
import streamlit as st


def make_prediction(input_data):
    """
    Predicts the presence or absence of cardiovascular disease based on input data.

    Parameters:
    input_data (dict): Dictionary containing input features for the model.
    """

    with open("model/random_forest_regressor.pkl", "rb") as model_file:
        model = pickle.load(model_file)

    # Convert input data to a DataFrame for prediction
    df_input_data = pd.DataFrame([input_data])

    # Predict the heart disease cluster
    prediction = model.predict(df_input_data)

    st.subheader("Heart Disease Prediction")

    if prediction[0] == 0:
        result_text = "Absence of cardiovascular disease"
        result_class = "absence"
    else:
        result_text = "Presence of cardiovascular disease"
        result_class = "presence"

    # Display the formatted result
    st.markdown(
        f'<div class="result-box {result_class}">{result_text}</div>',
        unsafe_allow_html=True,
    )

    # Predict the probability for each class
    pred_proba = model.predict_proba(df_input_data)[0]

    st.write(f"**Probability of absence:** `{pred_proba[0] * 100}%`")
    st.write(f"**Probability of presence:** `{pred_proba[1] * 100}%`")


    st.markdown(
        """
        <div class="note">
            Team Members
             <li>GHAVTE UBADA(720721104181)</li>
        </div>
        """,
        unsafe_allow_html=True,
    )
