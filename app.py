import streamlit as st
from modules.sidebar import sidebar
from modules.charts import (
    plot_radar_chart,
    display_shap_force_plot,
    display_numerical_distribution_chart,
    display_categorical_distribution_chart,
)
from modules.predict import make_prediction


def set_page_config():
    st.set_page_config(
        page_title="Heart Disease Predictor",
        page_icon="assets/heart_logo.png",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    with open("assets/style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


def display_header():
    st.title("Heart Disease Predictor")

    st.write(
        """
    This application uses machine learning to predict the presence or absence of cardiovascular disease based on input features such as age, height, weight, and blood pressure. 
    The radar chart provides a visual representation of the patient's health profile, while the predictions help in understanding the likelihood of cardiovascular disease. 
    """
    )


def main():
    set_page_config()
    input_dict = sidebar()

    with st.container():

        display_header()
        col1, col2 = st.columns([2, 1])

        with col1:
            # Radar Chart Function
            chart = plot_radar_chart(
                input_dict["age"],
                input_dict["height"],
                input_dict["weight"],
                input_dict["ap_hi"],
                input_dict["ap_lo"],
            )
            st.plotly_chart(chart)
        with col2:
            make_prediction(input_dict)

        st.title("Exploratory Data Analysis")
        display_shap_force_plot()
        display_numerical_distribution_chart()
        display_categorical_distribution_chart()


if __name__ == "__main__":
    main()
