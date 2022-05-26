from cProfile import label
import streamlit as st
import plotly_express as px 
import pandas as pd 

st.title('Data Visualization app')
# add sidebar
st.sidebar.subheader('Visualisation setting')

#setup file upload
#uploaded_file = st.sidebar.file_uploader(label="Upload your CSV file",
 #                         type=['CSV'])

#global df
#global numeric_columns
#if uploaded_file is not None:
    #print(uploaded_file)
    #print("Hello")             

df=pd.read_csv('Automobile_data.csv')
st.write(df)    
stock_column=df['Model']
unique_stock=stock_column.unique()

numeric_columns=list(df.select_dtypes(['float','int','object']).columns)
# add a select widget to the side bar
chart_select=st.sidebar.selectbox(
    label="Select the chart type",
    options=['Scatterplots','Lineplots','Histogram','Boxplot','AreaChart','BarChart']
)

if chart_select == 'Scatterplots':
    st.sidebar.subheader("Scatterplot Settings")
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        plot=px.scatter(data_frame=df,x=x_values,y=y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)


if chart_select == 'Lineplots':
    st.sidebar.subheader("Lineplots Settings")
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        plot=px.line(data_frame=df,x=x_values,y=y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Histogram':
    st.sidebar.subheader("Histogram Settings")
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        plot=px.histogram(data_frame=df,x=x_values,y=y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Boxplot':
    st.sidebar.subheader("Boxplot Settings")
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        plot=px.box(data_frame=df,x=x_values,y=y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'AreaChart':
    st.sidebar.subheader("AreaChart Settings")
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        plot=px.area(data_frame=df,x=x_values,y=y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'BarChart':
    st.sidebar.subheader("BarChart Settings")
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        plot=px.bar(data_frame=df,x=x_values,y=y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)


stock_dropdown = st.sidebar.selectbox(label='Car name',options=unique_stock)