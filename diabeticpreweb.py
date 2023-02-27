# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 22:16:21 2022

@author: Jyothsna
""" 

import numpy as np
import pickle
import streamlit  as st
import pandas as pd
import datetime
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://media.istockphoto.com/id/1222435595/photo/stethoscope-doctor-with-red-heart-on-black-wooden-table-background-with-space-for-text.jpg?s=170667a&w=0&k=20&c=0zQeepxTNXDKj7HSIISHKf9bdNChbg8_FWLnd3d49n0=");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
st.balloons()

Data_set = '<p style="font-family:Algerian; color:white; font-size: 40px;">DIABETIC PREDICTION WEB APP</p>'
st.markdown(Data_set, unsafe_allow_html=True)

Data_set = '<p style="font-family:Lucida Calligraphy; color:Cooper Black; font-size: 15px;">DATA SET</p>'
st.markdown(Data_set, unsafe_allow_html=True)
df=pd.read_csv("C:/Users/Jyothsna/Downloads/diabetes.csv")
st.write(df)
d = st.date_input(
    "When your checking",
    datetime.date(2019, 7, 6))
st.write('Your checking date is:', d)
t = st.time_input('Set time', datetime.time(8, 45))
st.write(' set for', t)




color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

dim=st.radio('What Dimenstions Do You Wnt to see?',('Rows','Columns','all'))
if dim=='Rows':
    st.text('Showing rows')
    st.write(df.shape[0])
if dim=='Columns':
    st.text('Showing Columns')
    st.write(df.shape[1])
else:
    st.text('Showing Shape of dataset')
    st.write(df.shape)
st.write('This is a area_chart.')
st.area_chart(df)
age=df['Age'].unique().tolist()
age1=st.selectbox('which age are you',age,0)
df=df[df["Age"]==age1]
fig=px.scatter(df,x='Pregnancies',y='BloodPressure',size='Glucose',color='SkinThickness',hover_name='Insulin',log_x=True,range_x=[100,1000],range_y=[30,90],animation_frame='Age',animation_group='BloodPressure')
fig.update_layout(width=800,height=600)
st.write(fig)
st.sidebar.header("STREAMLIT")
species_option = st.sidebar.selectbox('Select graphs',('linechart','Bar_chart','Pie_chart','Heat_map',))
if species_option == 'linechart':
    st.title('Linechart')
    st.line_chart(df['Pregnancies'])
if species_option == 'Bar_chart':
    st.title("Bar_chart")
    st.bar_chart(df[["SkinThickness","Glucose","Age","Insulin"]])
if species_option == 'Pie_chart':
    st.title("Pie_chart")
    cols = st.columns([1, 1])

    with cols[0]:
        medal_type = st.selectbox('Medal Type', ['Pregnancies', 'BloodPressure', 'Glucose'])
    
        fig = px.pie(df, values=medal_type, 
                 title=f'number of {medal_type} medals',
                 height=300, width=200)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0),)
        st.plotly_chart(fig, use_container_width=True)
if species_option == 'Heat_map':
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), ax=ax)
    st.write(fig)









loaded_model=pickle.load(open("C:/Users/Jyothsna/OneDrive/Desktop/test/trained_mode.sav",'rb'))
def diabetics_prediction(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if(prediction==[0]):
     return 'the person is not diabetic'
    else:
      return 'the person is diabetic'
def main():

    Pregnancies = st.slider('NO OF  Pregnancies', 0, 100, 1)

    Pregnancies=st.text_input("NO OF  Pregnancies")
    Glucose=st.text_input("NO OF Glucose ")
    BloodPressure=st.text_input("NO OF  bloodPressure")
    SkinThickness=st.text_input("NO OF  SkinThickness")
    Insulin=st.text_input("NO OF  Insulin")
    BMI=st.text_input("NO OF  SBMI")
    DiabetesPedigreeFunction=st.text_input("NO OF  DiabetesPedigreeFunction")
    Age=st.text_input("NO OF  Age")
    diagnosis=''
    if st.button('Diabetics test result'):
        diagnosis=diabetics_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success( diagnosis)
if __name__ == '__main__':
    main()
