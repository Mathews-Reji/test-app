import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict


st.title('GPS BASED TOLL COLLECTION')
st.markdown('A test model created for calculating the fees according to the distance travelled.')

st.header("Journey Details")
col1, col2 , col3 = st.columns(3)

with col1:
    st.text("Starting Point")
    start_x = st.text_input("Lattitude_start")
    start_y = st.text_input("Longitude_start")
    


with col2:
    st.text("End Points")
    end_x=st.text_input("Lattitude_end")
    end_y = st.text_input("Longitude_end")

with col3:
    st.text("Other Details")
    distance=st.text_input("Enter The Distance")
    vehicle_id=st.text_input("Enter The Vehicle ID")
    average_speed=st.slider('Kmph', min_value=0, max_value=150)


st.text('')
if st.button("Calculate Fee"):
    result = predict(np.array([start_x,start_y,end_x,end_y,distance,vehicle_id,average_speed]))
    st.text(result[0])
