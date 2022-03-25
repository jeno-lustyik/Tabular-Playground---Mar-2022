import numpy as np
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim
import plotly
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

df_train = pd.read_csv('data/train.csv').drop(['row_id'], axis=1)
df_train['year'] = df_train['time'].apply(lambda row: row[:4])
df_train['month'] = df_train['time'].apply(lambda row: row.split('-')[1][:2])
df_train['day'] = df_train['time'].apply(lambda row: row.split('-')[2][:2])
df_train['hour'] = df_train['time'].apply(lambda row: row.split(':')[0][-2:])
df_train['mins'] = df_train['time'].apply(lambda row: row.split(':')[1])
df_train['d'] = df_train['time'].apply(lambda row: row.split(':')[0])
df_train['dates'] = df_train['time'].apply(lambda row: row[:-9].split('-')[:3])
df_train['dates'] = df_train['dates'].apply(lambda row: datetime(int(row[0]), int(row[1]), int(row[2])))
df_train['weekdays'] = df_train['dates'].apply(lambda row: row.weekday())



st.title('Tabular Playground Series - Mar 2022')
st.subheader('Exploratory Data Analysis')

st.text(
    """We're investigating the data of the traffic congestion across 65
roadways between April and September in 1991, in a US Metropolitan city.
""")

# fig_bar_direction = px.bar(df_train, x='direction', y='congestion')

st.subheader('Congestion in different directions')
st.text(
    """We can investigate in which direction the traffic is most common, as we can see,
    northbound and southbound traffic is the most frequent.
""")

df_train_sort_direction = df_train.sort_values(by='congestion')

fig_directions = plt.figure(figsize=(10, 4))
fig = sns.barplot(x='direction', y='congestion', data=df_train_sort_direction, palette='plasma')
fig.set_xlabel('Directions', fontsize=15)
fig.set_ylabel('Congestion', fontsize=15)
fig.set_title('Direction Vs Congestion', fontsize=20)
st.pyplot(fig_directions)

st.subheader('Congestion on different days')
st.text(
    """We can investigate which days are the most congested.
    We can see a small drop during the weekends when people take their time to rest.
""")

fig_directions = plt.figure(figsize=(10, 4))
fig = sns.barplot(x='weekdays', y='congestion', data=df_train, palette='plasma')
fig.set_xlabel('Weekdays', fontsize=15)
fig.set_ylabel('Congestion', fontsize=15)
fig.set_title('Congestion on different days', fontsize=20)
fig.set_xticklabels(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], fontsize=10)
st.pyplot(fig_directions)

st.subheader('Congestion at different hours')
st.text(
    """We can investigate which parts of the day are the most congested.
    There's a difference between the two rush-hour congestions,
    and we can inspect that by splitting the data by weekdays and weekends.
""")


fig_directions = plt.figure(figsize=(10, 4))
fig = sns.barplot(x='hour', y='congestion', data = df_train, palette='plasma')
fig.set_xlabel('Hours', fontsize=15)
fig.set_ylabel('Congestion', fontsize=15)
fig.set_title('Congestion at different hours', fontsize=20)
st.pyplot(fig_directions)

st.text(
    """By splitting the data to weekends and weekdays, we can see
    an increase in the congestion on weekdays during the morning rush hour period
    and a decrease in the weekend during the morning hours.
    We can also see that the weekends have a more evenly spread out graph,
    as the nightlife blooms on Saturdays.
""")

fig_directions = plt.figure(figsize=(10, 4))
fig = sns.barplot(x=df_train['hour'].loc[df_train['weekdays'] < 5], y='congestion', data = df_train, palette='plasma')
fig.set_xlabel('Hours', fontsize=15)
fig.set_ylabel('Congestion', fontsize=15)
fig.set_title('Congestion on weekdays', fontsize=20)
st.pyplot(fig_directions)

fig_directions = plt.figure(figsize=(10, 4))
fig = sns.barplot(x=df_train['hour'].loc[df_train['weekdays'] > 4], y='congestion', data = df_train, palette='plasma')
fig.set_xlabel('Hours', fontsize=15)
fig.set_ylabel('Congestion', fontsize=15)
fig.set_title('Congestion on weekends', fontsize=20)
st.pyplot(fig_directions)