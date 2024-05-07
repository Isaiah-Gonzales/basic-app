import streamlit as st

st.title("Artificial Neural Network: Roller Compactor Tool")

predictor = st.selectbox('what would you like to predict:', ('flowability (I have a target solid fraction and roll pressure in mind)','roll pressure (I have a target solid fraction and flowability in mind)')

drug = st.selectbox('Please select your drug:', ('ibupfrofen', 'metformin', 'input my own drug characteristics'))

if drug == 'input my own drug characteristics':
        drug_d90 = st.text_input('drug d90')
        ib_bulk_d = st.text_input('initial blend bulk density')
        ib_flow_rate = st.text_input('initial blend flow rate')

target_solid_fraction = st.text_input('target solid fraction (default 0.7):', value = 0.7)

