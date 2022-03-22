import numpy as np
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim
import plotly
df_train = pd.read_csv('data/train.csv').drop(['row_id'], axis=1)


st.title('Tabular Playground Series - Mar 2022')
st.subheader('Exploratory Data Analysis')

st.text(
"""We're investigating the data of the traffic congestion across 65
roadways between April and September in 1991.
""")

fig_bar_direction = px.bar(df_train, x='direction', y='congestion')
st.plotly_chart(fig_bar_direction)
