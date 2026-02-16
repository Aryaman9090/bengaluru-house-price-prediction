import streamlit as st
import joblib
import pandas as pd
import numpy as np
model = joblib.load("ben_house_price_model.pkl")

st.header("Bengaluru house price prediction")
area_type = st.selectbox("Select your area",["super built-up  area","built-up  area","plot  area","carpet  area"])
ava = st.selectbox("Availability",["Not Moved","Ready to move"])
location = st.text_input("Enter location ")
total_sqft = st.number_input("Enter total_sqft")
bath = st.slider("Number of bath",min_value = 0 ,max_value =30)
balcony = st.slider("Number of balcony",min_value = 0 ,max_value =3)
bhk = st.slider("Number of bhk",min_value = 0 ,max_value =3)


real = pd.DataFrame({
    "area_type": [area_type],
    "availability": [ava],
    "location": [location],
    "total_sqft": [total_sqft],
    "bath": [bath],
    "balcony": [balcony],
    "bhk": [bhk]
})


if st.button("Predicted"):
    pred = model.predict(real)
    og = np.expm1(pred)
    st.success("According to this data your estimated price is " + str(og))


















