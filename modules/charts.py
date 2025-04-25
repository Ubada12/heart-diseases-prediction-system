import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from modules.data import get_data

data = get_data()


def plot_radar_chart(age, height, weight, ap_hi, ap_lo):
    categories = [
        "Age (days)",
        "Height (cm)",
        "Weight (kg)",
        "Systolic BP (ap_hi)",
        "Diastolic BP (ap_lo)",
    ]
    values = [age, height, weight, ap_hi, ap_lo]

    # Normalize values for better radar visualization
    max_values = [150, 250, 200, 200, 150]
    normalized_values = [val / max_val * 5 for val, max_val in zip(values, max_values)]

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=normalized_values,
            theta=categories,
            fill="toself",
            name="User Input",
            fillcolor="rgba(255, 0, 0, 0.5)",
            line_color="rgba(255, 0, 0, 0.8)",
        )
    )

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
        showlegend=False,
        title="Radar Chart of Health Metrics",
    )

    return fig


def display_shap_force_plot():

    st.markdown("1. **SHAP Force Plot**")

    html_content = (
        """
        <style>
       .tick text  {
            fill: white !important;
        }
        .force-bar-axis path{
            color: white !important;
        }
        </style>
        
    """
        + open("./assets/shap_force_plot.html", "r", encoding="utf-8").read()
    )

    components.html(html_content)

    st.write(
        """
    The plot shows how each feature contributes to the prediction (represented by the arrow length and direction). 
    Positive values (red) indicate features pushing the prediction higher, while negative values (blue) push it lower.
    """
    )


def display_numerical_distribution_chart():

    fig = make_subplots(rows=4, cols=1)
    fig.add_trace(go.Box(x=data["age"], name="Age"), row=1, col=1)
    fig.add_trace(go.Box(x=data["weight"], name="weight"), row=2, col=1)
    fig.add_trace(go.Box(x=data["ap_hi"], name="Systolic blood pressure"), row=3, col=1)
    fig.add_trace(
        go.Box(x=data["ap_lo"], name="Diastolic blood pressure"), row=4, col=1
    )
    fig.update_layout(
        height=700,
        template="plotly_dark",
        title="2. Numerical distributions of Health Metrics",
        showlegend=False
    )

    st.plotly_chart(fig)
    st.markdown(
        """
    This chart shows the distribution of numerical health metrics.
    Each box plot provides insights into the variability and central tendency of these health metrics.
    """
    )
    


def display_categorical_distribution_chart():

    fig = make_subplots(rows=2, cols=3)
    fig.add_trace(go.Bar(y=data["gender"].value_counts(), x=["Female", "Male"], name="Gender"), row=1, col=1)
    fig.add_trace(go.Bar(y=data["cholesterol"].value_counts(), x=["Normal", "Above Normal", "Well Above Normal"], name="Cholesterol"), row=1, col=2)
    fig.add_trace(go.Bar(y=data["gluc"].value_counts(), x=["Normal", "Above Normal", "Well Above Normal"], name="Glucose"), row=1, col=3)
    fig.add_trace(go.Bar(y=data["smoke"].value_counts(), x=["Non-Smoker", "Smoker"], name="Smoker"), row=2, col=1)
    fig.add_trace(go.Bar(y=data["alco"].value_counts(), x=["Non-Alcoholic", "Alcoholic"], name="Alcoholic"), row=2, col=2)
    fig.add_trace(go.Bar(y=data["active"].value_counts(), x=["Inactive", "Active"], name="Active"), row=2, col=3)
    fig.update_layout(
        template="plotly_dark",
        height=700,
        title="3. Categorical distributions of Health Metrics",
        legend=dict(
            orientation="h",  # Place legend horizontally
            xanchor="right",
            x=1
        )
    )

    st.plotly_chart(fig)
    st.markdown(
        """
    This chart displays categorical distributions.
    Each bar chart provides a categorical view of these attributes, highlighting their prevalence or distribution.
    """
    )
    
