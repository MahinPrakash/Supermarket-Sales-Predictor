import streamlit as st
import numpy as np
import pandas as pd
import pickle

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown("<h1 style='text-align:center;'>Super Market Sales Predictor</h1>",unsafe_allow_html=True)

item_weight = st.number_input("Item Weight:")
options = ["regular","low_fat"]
fat_content = st.selectbox("Item Fat Content:", options)
if (fat_content=="regular"):
    fat_content=1.0
else:
     fat_content=0.0    
visibility = st.text_input("Item Visibility:", value="0.0")
ioptions = ["Drinks","Food",'Non-Consumable']
item_type = st.selectbox("Item Type:", ioptions)
if (item_type=="Drinks"):
    item_type=0.0
elif(item_type=="Food"):
     item_type=1.0
else:
     item_type=2.0
mrp = st.number_input("MRP:")
year=st.number_input("Years of Operation:", step=1, format="%d")
soptions = ["Small","Medium",'High']
outlet_size = st.selectbox("Outlet Size:", soptions)
if (outlet_size=="Small"):
     outlet_size=2.0
elif(outlet_size=="Medium"):
     outlet_size=1.0
else:
     outlet_size=0.0
oloptions = ["Tier 1","Tier 2",'Tier 3']
o_location_type = st.selectbox("Outlet Location Type:",oloptions)
if (o_location_type=="Tier 1"):
     o_location_type=0.0
elif(o_location_type=="Tier 2"):
     o_location_type=1.0
else:
     o_location_type=2.0
otoptions = ["Grocery Store","Supermarket Type1",'Supermarket Type2',"Supermarket Type3"]
o_types = st.selectbox("Outlet Types:",otoptions)
if(o_types=="Grocery Store"):
     o_types=0.0
elif(o_types=="Supermarket Type1"):
     o_types=1.0
elif(o_types=="Supermarket Type2"):
     o_types=2.0
else:
     o_types=3.0
x=[[item_weight,fat_content,visibility,item_type,mrp,
                  year,outlet_size,o_location_type,o_types ]]
# model_path='sales_predictor.sav'
# model= joblib.load(model_path)
with open( 'prediction_model', 'rb') as f:
    model=pickle.load(f)
result=model.predict(x)[0]
col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    submit_button = st.button('Predict')
if submit_button:
     st.success(f"Item Outlet Sales = {result.round(1)}")
