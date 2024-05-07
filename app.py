import streamlit as st

st.title("Artificial Neural Network: Flowability Predictor")

drug = st.selectbox('Please select your drug:', ('ibupfrofen', 'metformin', 'input my own drug characteristics'))

target_solid_fraction = st.text_input('target solid fraction (default 0.7):', value = 0.7)
        
