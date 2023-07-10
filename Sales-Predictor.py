import streamlit as st
import numpy as np
import pandas as pd
import pickle
import joblib
st.markdown(
    """
    <style>
        [class="css-18ni7ap e8zbici2"]{
           visibility: hidden;
        }
        .css-12oz5g7{
           padding-top:0rem;
        }
        [class="main css-1v3fvcr egzxvld3"] {
          background-image: url('https://img.freepik.com/free-photo/vivid-blurred-colorful-background_58702-2654.jpg?w=900&t=st=1688727986~exp=1688728586~hmac=b3ac94b60d2c35089e2fbf7c0d788792afef6e32ef3db90df0eb54d338d36923');
          background-size: cover;
        }
        [data-testid="stHeader"]{
        background-color:rgba(0,0,0,0);
        }
        [class="css-1cpxqw2 edgvbvh9"]{
          text-align:center
        }
        [class="css-1q1n0ol egzxvld0"]{
          visibility: hidden;
        }
        [data-testid="stMarkdownContainer"]{
          font-size:24px
        }
    </style>
    """,
    
    unsafe_allow_html=True,
)


st.markdown("<h1 style='text-align:center;'>Sales Predictor</h1>",unsafe_allow_html=True)

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
