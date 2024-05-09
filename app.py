import streamlit as st
import tensorflow as tf


st.title("Artificial Neural Network: Roller Compactor Tool")
st.text("beta version: fixed drug load % and roll gap")

predictor = st.selectbox('what would you like to predict:', ('Flowability (I have a target solid fraction and roll pressure in mind)','Roll Pressure (I have a target solid fraction and flowability in mind)'))

drug = st.selectbox('Please select your drug:', ('ibupfrofen', 'metformin', 'input my own drug characteristics'))

if drug == 'input my own drug characteristics':
        drug_d90 = st.text_input('drug d90')
        ib_bulk_d = st.text_input('initial blend bulk density')
        ib_flow_rate = st.text_input('initial blend flow rate')
        ib_true_d = st.text_input('intial blend flow rate')

target_solid_fraction = st.text_input('target solid fraction (default 0.7):', value = 0.7)
target_flowability = st.text_input('target flowability (seconds/100g): (default 33.7)')

if st.button('predict my required roll pressure'):
        st.markdown('predicted required roll pressure is: **47**')
