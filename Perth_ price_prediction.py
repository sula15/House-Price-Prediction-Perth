import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image

model = pickle.load(open("/Users/sulaknaweerasinghe/Documents/sliit/y3/s1/FDM/mini project/webapp/model5.sav", 'rb'))

st.title('Perth House Price Prediction')
st.sidebar.header('House Details')
image = Image.open('/Users/sulaknaweerasinghe/Documents/sliit/y3/s1/FDM/mini project/webapp/perth.jpg')
st.image(image, '')


# FUNCTION
def house_price():
    BEDROOMS = st.sidebar.slider('Bedrooms', 1, 10, 1)
    LAND_AREA = st.sidebar.slider('Land area (sq.m)', 60, 3000, 60)
    FLOOR_AREA = st.sidebar.slider('Floor area (sq.m)', 60, 900, 60)
    BUILD_YEAR = st.sidebar.slider('Build year', 1970, 2020, 1970)
    SOLD_YEAR = st.sidebar.slider('Sold year', 2014, 2021, 2014)
    POSTCODE = st.sidebar.slider('Postcode', 6003, 6160, 6003)
    GARAGE = st.sidebar.slider('garage space', 0, 5, 0)
    NEAREST_SCH_RANK = st.sidebar.slider('nearest school rank', 1, 139, 1)
    CBD_DIST = st.sidebar.slider('Distance to Central Business District (m)', 680, 6000, 680)

    house_price_data = {
        'BEDROOMS': BEDROOMS,
        'LAND_AREA': LAND_AREA,
        'FLOOR_AREA': FLOOR_AREA,
        'BUILD_YEAR': BUILD_YEAR,
        'SOLD_YEAR': SOLD_YEAR,
        'POSTCODE': POSTCODE,
        'GARAGE': GARAGE,
        'NEAREST_SCH_RANK': NEAREST_SCH_RANK,
        'CBD_DIST': CBD_DIST

    }
    house_price_data = pd.DataFrame(house_price_data, index=[0])
    return house_price_data


house_data = house_price()
st.header('House Details')
st.write(house_data)

price = model.predict(house_data)
st.subheader('Predicted house price')
st.subheader('$' + str(np.round(price[0], 2)))
