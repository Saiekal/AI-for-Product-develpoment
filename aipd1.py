import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("mental_health_model.pkl", "rb"))

st.title("Student Mental Health Risk Predictor")

academic_workload = st.slider("Academic Workload", 1, 5)
academic_pressure = st.slider("Academic Pressure", 1, 5)
financial_concerns = st.slider("Financial Concerns", 1, 5)
social_relationships = st.slider("Social Relationships", 1, 5)
study_satisfaction = st.slider("Study Satisfaction", 1, 5)


if st.button("Predict"):
    input_data = np.array([[academic_workload,
                            academic_pressure,
                            financial_concerns,
                            social_relationships,
                            study_satisfaction
                            ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Mental Health Risk")
    else:
        st.success("Low Mental Health Risk")