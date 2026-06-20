import streamlit as st
import pickle 
import numpy as np

#load the trained model
with open('crop_model.pkl','rb') as file:
	model=pickle.load(file)

st.title("🌿 Crop Recommendation system")
st.write("Enter your soil and weather details to get a crop recommendation.")

#Input fields
N=st.number_input("Nitrogen(N)",min_value=0,max_value=140,value=0)
P=st.number_input("Phosphorus(P)",min_value=0,max_value=145,value=0)
K=st.number_input("Potassium(K)",min_value=0,max_value=205,value=0)
temperature=st.number_input("Temperature(°C)",min_value=0.0,max_value=50.0,value=0.0)
humidity=st.number_input("Humidity(%)",min_value=0.0,max_value=100.0,value=0.0)
ph=st.number_input("pH",min_value=0.0,max_value=14.0,value=0.0)
rainfall=st.number_input("Rainfall(mm)",min_value=0.0,max_value=300.0,value=0.0)

if st.button("Recommend Crop"):
	sample=np.array([[N,P,K,temperature,humidity,ph,rainfall]])
	prediction=model.predict(sample)
	st.success(f"Recommended Crop : **{prediction[0].capitalize()}**")