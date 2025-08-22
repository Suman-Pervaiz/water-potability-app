import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("water_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💧 Water Potability Prediction App")
st.write("Enter the water quality parameters below to check if the water is potable or not.")

# Input fields
ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1)
hardness = st.number_input("Hardness", min_value=0.0, step=0.1)
solids = st.number_input("Solids", min_value=0.0, step=0.1)
chloramines = st.number_input("Chloramines", min_value=0.0, step=0.1)
sulfate = st.number_input("Sulfate", min_value=0.0, step=0.1)
conductivity = st.number_input("Conductivity", min_value=0.0, step=0.1)
organic_carbon = st.number_input("Organic Carbon", min_value=0.0, step=0.1)
trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, step=0.1)
turbidity = st.number_input("Turbidity", min_value=0.0, step=0.1)

# Prediction button
if st.button("Predict Potability"):
    # Arrange values as model input
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                            conductivity, organic_carbon, trihalomethanes, turbidity]])

    # Make prediction
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ The water is **Potable** (Safe to drink)")
    else:
        st.error("❌ The water is **Not Potable** (Unsafe to drink)")

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        right: 0;
        color: gray;
        font-size: 22px;
        padding: 5px 10px;
    }
    </style>
    <div class="footer">App by Suman Pervaiz</div>
    """,
    unsafe_allow_html=True
)

