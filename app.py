import streamlit as st
import tensorflow as tf


st.title("Artificial Neural Network: Roller Compactor Tool")
st.text("beta version: fixed drug load % and roll gap")

predictor = st.selectbox('what would you like to predict:', ('Flowability','Roll Pressure'), help='**Flowability** assumes you have a target roll pressure and solid fraction, while **Roll Pressure** assumes you have a target flowability and solid fraction)

drug = st.selectbox('Please select your drug:', ('ibupfrofen', 'metformin', 'input my own drug characteristics'))

if drug == 'input my own drug characteristics':
        drug_d90 = st.text_input('drug d90')
        ib_bulk_d = st.text_input('initial blend bulk density')
        ib_flow_rate = st.text_input('initial blend flow rate')
        ib_true_d = st.text_input('intial blend flow rate')

target_solid_fraction = st.text_input('target solid fraction:', value = 0.7, help='default is conventional target solid fraction')
target_flowability = st.text_input('target flowability (seconds/100g):',value = 33.7, help='default is the flowability of a placebo blend')

if st.button('predict my required roll pressure'):
        st.markdown('predicted required roll pressure is: **47**')
