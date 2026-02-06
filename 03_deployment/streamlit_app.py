import streamlit as st
import pickle
import numpy as np
import pandas as pd


with open('model/catboost_price_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)
    
st.title("🏠 ImmoEliza House Price Prediction")

# Input fields

bedroomCount = st.number_input("Number of Bedrooms", min_value=0, value=2)
toilet_and_bath = st.number_input("Toilets/Bathrooms", min_value=0, value=1)
habitableSurface = st.number_input("Habitable Surface (m²)", min_value=10, value=100)
facedeCount = st.number_input("Number of Facades", min_value=1, value=2)
hasTerrace = st.checkbox("Has Terrace?")
totalParkingCount = st.number_input("Parking Count", min_value=0, value=1)
type= st.selectbox("Property Type", ["APARTMENT", "HOUSE"])
subtype = st.selectbox("Subtype", ["DUPLEX", "VILLA", "PENTHOUSE", "BUNGALOW"])
province = st.selectbox("Province", ["Brussels", "Antwerp", "East Flanders", "West Flanders", "Limburg", "Namur", "Liege"])
locality = st.text_input("Locality (e.g. Etterbeek)", "Etterbeek")
postCode = st.number_input("Number of Bedrooms", min_value=0, value=1000)
buildingCondition = st.selectbox("Building Condition", ["NEW" , "GOOD" , "TO RENOVATE" , "JUST RENOVATED" , "TO REBUILD",""])
epcScore= st.selectbox("epcscore",["A","B","C","D","E","F","G",""])

input_data = {
    "bedroomCount": bedroomCount,
    "toilet_and_bath": toilet_and_bath,
    "habitableSurface": habitableSurface,
    "facedeCount": facedeCount,
    "hasTerrace": hasTerrace,
    "totalParkingCount": totalParkingCount,
    "type": type,
    "subtype": subtype,
    "province": province,
    "locality": locality,
    "postCode": postCode,
    "buildingCondition": buildingCondition,
    "epcScore": epcScore
}
# When button is clicked
if st.button("Predict Price"):
        
    try:  
        df=pd.DataFrame([input_data]) 
        prediction = model.predict(df)
        st.success(f"Predicted Price: €{prediction[0]:,.2f}")
        
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")