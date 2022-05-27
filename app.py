from cProfile import label
import streamlit as st
import plotly_express as px 
import pandas as pd 
from PIL import Image 

st.title('Automotive Industry')
# add sidebar
st.sidebar.subheader('Visualisation setting')

#upload image

img = Image.open("car.png")
st.image(img,width=600)

#about automotive industry
#st.button("Know about auotmotive industry")
if st.button("About"):
    st.text("automotive industry, all those companies and activities involved in the manufacture of motor vehicles, "
            " including most components, such as engines and bodies, but excluding tires, batteries, and fuel. The"
            "industry’s principal products are passenger automobiles and light trucks, including pickups, vans,"
            " and sport utility vehicles.")

#Users detail
name=st.text_input("Enter your name","type here...")
address= st.text_input("Enter your favourite Car","Type here..")

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
    st.sidebar.subheader("Scatterplots Settings")
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

#Radio
st.write("## Car Types")
status = st.radio("What is your Car type?",("Sedan","Coupe","Hatchback","Wagon","Sports_Car","Minivan","SUV"))
if status == 'Sedan':
    img = Image.open("Sedan.png")
    st.image(img,width=400)
    st.success("These cars have a separate area for keeping luggage. Sedans are loved by many. They are typically four door cars with seating capability of 4 + people")

if status == 'Coupe':
    img = Image.open("Coupe.png")
    st.image(img,width=400)
    st.success("These are small cars but are admired for their sport looks. They have the seating capability for two to four people. It is usually equipped with two doors with a small boot.")

if status == 'Hatchback':
    img = Image.open("hatch.png")
    st.image(img,width=400)
    st.success("It refers to the car which has an additional space for cargo. These cars have a large door at the backside of the car, which gives access to this additional area.")

if status == 'Wagon':
    img = Image.open("Wagon.png")
    st.image(img,width=400)
    st.success("hese are also known as Estate Car. They are quiet similar to a hatchback but with an extended roof and rear body. This extra space makes it eligible for adding the third row.")

if status == 'Sports_Car':
    img = Image.open("Sports_car.png")
    st.image(img,width=400)
    st.success("These are the sportiest, hottest, coolest-looking coupes and convertibles—low to the ground, sleek, and often expensive. They generally are two-seaters, but sometimes have small rear seats as well.")

if status == 'Minivan':
    img = Image.open("Minivan.png")
    st.image(img,width=400)
    st.success(" These are smaller version of vans which are structured on car platforms. These vans have sliding rear doors. These are included in the segment of mid-sized cars.")

if status == 'SUV':
    img = Image.open("SUV.png")
    st.image(img,width=400)
    st.success("These cars are known for their off-road capabilities. They have a large body type. Their seating capacity ranges from 5 to 7+.")

st.write("## Your favourite Car")
car = st.multiselect("Which car you would like to buy?" ,("alfa-romero","audi","BMW","chevrolet",
"dodge","honda","isuzu","jaguar","mazda","mercedes-benz","mitsubishi","nissan","peugot","plymouth","porsche","saab",
"subaru","toyota","volkswagen","volvo"))
st.write("You selected" , car)

