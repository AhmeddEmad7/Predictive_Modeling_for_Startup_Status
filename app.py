import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn

st.title('Predicting a Startup’s Acquisition Status')
st.image('company-status-active.png')


#Load data
df = pd.read_csv('Cleaned_data.csv')
model = pd.read_pickle('Model.pkl')

#App



funding_rounds = st.number_input('funding rounds', min_value=df['funding_rounds'].min(), max_value=df['funding_rounds'].max())
funding_total_usd = st.number_input('funding total usd', min_value=df['funding_total_usd'].min(), max_value=df['funding_total_usd'].max())
lat = st.number_input('latitude', min_value=df['lat'].min(), max_value=df['lat'].max())
lng = st.number_input('longitude', min_value=df['lng'].min(), max_value=df['lng'].max())
relationships = st.number_input('relationships', min_value=df['relationships'].min(), max_value=df['relationships'].max())

new_data = {'funding_rounds':funding_rounds,'funding_total_usd':funding_total_usd,
            'lat':lat,'lng':lng ,'relationships':relationships }

new_data = pd.DataFrame(new_data,index=[0])

status = model.predict(new_data)

# Output
if st.button('Predict'):
    st.markdown('## Status:')
    st.markdown(status)
