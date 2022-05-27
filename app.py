from cProfile import label
import streamlit as st
import plotly_express as px 
import pandas as pd 
from PIL import Image 


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('Automotive Industry')
# add sidebar
st.sidebar.subheader('Visualisation setting')

#upload image

img = Image.open("car.png")
st.image(img,width=600)

#about automotive industry
#st.button("Know about auotmotive industry")
if st.button("About"):
    st.success("automotive industry, all those companies and activities involved in the manufacture of motor vehicles, "
            " including most components, such as engines and bodies, but excluding tires, batteries, and fuel. The"
            "industry’s principal products are passenger automobiles and light trucks, including pickups, vans,"
            " and sport utility vehicles.")

#Users detail
first, last = st.columns (2)
first.text_input("First Name")
last.text_input ("Last Name")


email, mob= st.columns([3,1])
email.text_input ("Email ID")
mob.text_input ("Mob Number")


address= st.text_input("Enter your favourite Car","Type here..")

ch,bl,sub=st.columns(3)
sub.button("Submit")
#setup file upload
#uploaded_file = st.sidebar.file_uploader(label="Upload your CSV file",
 #                         type=['CSV'])

#global df
#global numeric_columns
#if uploaded_file is not None:
    #print(uploaded_file)
    #print("Hello")             

df=pd.read_csv('Automobile_data.csv')

check_box=st.sidebar.checkbox(label="Display Dataset")
if check_box:
    st.write(df)    

st.write("### Graph of all type of data in dataset")
numeric_columns=list(df.select_dtypes(['float','int','object']).columns)



# add a select widget to the side bar
chart_select=st.sidebar.selectbox(
    label="Select the chart type",
    options=['Scatterplots','Lineplots','Histogram','Boxplot','AreaChart','BarChart','violinPlot']
)

if chart_select == 'Scatterplots':
    st.sidebar.subheader("Scatterplots Settings")
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        color_R=st.sidebar.selectbox('color',options=numeric_columns)
        plot=px.scatter(data_frame=df,x=x_values,y=y_values,color=color_R)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)


if chart_select == 'Lineplots':
    st.sidebar.subheader("Lineplots Settings")
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        color_R=st.sidebar.selectbox('color',options=numeric_columns)
        plot=px.line(data_frame=df,x=x_values,y=y_values,color=color_R)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Histogram':
    st.sidebar.subheader("Histogram Settings")
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        color_R=st.sidebar.selectbox('color',options=numeric_columns)
        plot=px.histogram(data_frame=df,x=x_values,y=y_values,color=color_R)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Boxplot':
    st.sidebar.subheader("Boxplot Settings")
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        color_R=st.sidebar.selectbox('color',options=numeric_columns)
        plot=px.box(data_frame=df,x=x_values,y=y_values,color=color_R)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'AreaChart':
    st.sidebar.subheader("AreaChart Settings")
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        color_R=st.sidebar.selectbox('color',options=numeric_columns)
        plot=px.area(data_frame=df,x=x_values,y=y_values,color=color_R)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'BarChart':
    st.sidebar.subheader("BarChart Settings")
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        color_R=st.sidebar.selectbox('color',options=numeric_columns)
        plot=px.bar(data_frame=df,x=x_values,y=y_values,color=color_R)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'violinPlot':
    st.sidebar.subheader("Violinlots Settings")
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        color_R=st.sidebar.selectbox('color',options=numeric_columns)
        plot=px.violin(data_frame=df,x=x_values,y=y_values,color=color_R)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)




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
car = st.selectbox("Which car you would like to buy?" ,("alfa-romero","audi","BMW","chevrolet",
"dodge","honda","isuzu","jaguar","mercedes-benz","nissan","peugot","subaru","toyota","volvo"))
#st.write('you selected: ', car)

if car == 'alfa-romero':
    st.write("Know about your car by clicking the link")
    st.write("https://en.wikipedia.org/wiki/Alfa_Romeo#:~:text=Alfa%20Romeo%20Automobiles%20S.p.A.%20(Italian,%22Anonima%20Lombarda%20Fabbrica%20Automobili.%22")
    st.write("https://www.youtube.com/watch?v=6Sd_fmHVX_o")

if car == 'audi':
    st.write("Know about your car by clicking the link")
    st.write("https://en.wikipedia.org/wiki/Audi")
    st.write("https://www.youtube.com/watch?v=9pQ9E4k8uck")

if car == 'BMW':
    st.write("Know about your car by clicking the link")
    st.write("https://en.wikipedia.org/wiki/BMW")
    st.write("https://www.youtube.com/watch?v=x8POsG-7Z3w")

if car == 'chevrolet':
    st.write("Know about your car by clicking the link")
    st.write("https://en.wikipedia.org/wiki/Chevrolet")
    st.write("https://www.youtube.com/watch?v=bOzGmhMqzv4")

if car == 'dodge':
    st.write("Know about your car by clicking the link")
    st.write("https://en.wikipedia.org/wiki/Dodge")
    st.write("https://www.youtube.com/watch?v=Mi6dUNkZlM8")

if car == 'honda':
    st.write("Know about your car by clicking the link")
    st.write("https://en.wikipedia.org/wiki/Honda")
    st.write("https://www.youtube.com/watch?v=U17zDef8UTs")

if car == 'jaguar':
    st.write("Know about your car by clicking the link")
    st.write("https://en.wikipedia.org/wiki/Jaguar_Cars")
    st.wrie("https://www.youtube.com/watch?v=_-3Qf29iaHw")

if car == 'mercedes-benz':
   st.write("Know about your car by clicking the link")
   st.write("https://en.wikipedia.org/wiki/Mercedes-Benz")
   st.write("https://www.youtube.com/watch?v=t6TIShBd3Hw")

if car == 'nissan':
    st.write("Know about your car by clicking the link")
    st.write("https://en.wikipedia.org/wiki/Nissan")
    st.write("https://www.youtube.com/watch?v=j1nlT-0mXNU")

if car == 'peugot':
    st.write("Know about your car by clicking the link")
    st.write("https://en.wikipedia.org/wiki/Peugeot")
    st.write("https://www.youtube.com/watch?v=xJm53cAgtiE")

if car =='subaru':
    st.write("Know about your car by clicking the link")
    st.write("https://en.wikipedia.org/wiki/Subaru")
    st.write("https://www.youtube.com/watch?v=3Wr7ZpFL3Ag")

if car == 'toyota':
    st.write("Know about your car by clicking the link")
    st.write("https://en.wikipedia.org/wiki/Toyota")
    st.write("https://www.youtube.com/watch?v=CLnY78Z7bwU")

if car == 'volvo':
    st.write("Know about your car by clicking the link")
    st.write("https://en.wikipedia.org/wiki/Volvo_Cars")
    st.write("https://www.youtube.com/watch?v=yTWMwxD5Y3I")



