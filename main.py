import streamlit as st
import urllib.request
from PIL import Image
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

st.title("AUTOMOBILE INDUSTRY")

img = Image.open("car.png")
st.image(img, width=600)
st.write('## Dataset')
Car_data=pd.read_csv('Automobile_data.csv')
#st.write(Car_data.head())
st.dataframe(Car_data)

st.write('## Chart Elements')

st.write('#### Line Chart')
df = pd.DataFrame(
     np.random.randn(20, 1),
     columns=['price'])

st.line_chart(df.head(10))

st.write('#### Histogram')
arr = np.random.normal(1, 1, size=100)
df, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(df)

genre = st.radio(
     "What's your favorite Car",
     ('Toyota', 'audi', 'honada'))

st.button("Click to know about Automotive_industry")
if(st.button("About")):

    st.text_area("The automotive industry comprises a wide range of companies and organizations involved in the design, development, manufacturing, marketing, and selling of motor vehicles. It is one of the world's largest industries by revenue (from 16 % such as in France up to 40 % to countries like Slovakia).")

st.snow()
group_column = st.selectbox(
     'What would you like to analyse?',
     ('Model','engine-size','body-style','price')
)


output_column = ['num-of-doors','horsepower']
df_grouped = df.groupby(by=[group_column], as_index=False)[output_column].count()
st.dataframe(df_grouped)