# 🌾 Crop Recommendation System

A machine learning web app that recommends the most suitable crop based on soil and weather conditions. Built during my AI & ML internship at Marcello Tech, Trichy.

## Live App
https://crop-recommendation-vassumitha.streamlit.app/

## Features
- Takes 7 inputs: N, P, K, temperature, humidity, pH and rainfall
- Predicts the best crop using a trained ML model
- Simple Streamlit interface

## Files
- app_internship_version.py: Streamlit app
- crop_model.pkl: trained model
- requirements.txt: dependencies

## Tech Stack
Python, Streamlit, NumPy, scikit-learn

## Run Locally
pip install -r requirements.txt
streamlit run app_internship_version.py

## Future Scope
- Add crop images and growing tips
- Fertilizer recommendations