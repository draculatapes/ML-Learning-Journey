import streamlit as st
import pandas as pd
st.title("Streamlite Text Input")
name=st.text_input('Enter your name: ')

age=st.slider('Select Your age: ',0,100,25)
st.write(f"your age is {age}")

options=["python","java","c++","javascript"]
choice=st.selectbox("chose you fav lang",options)
st.write(f"you have selected {choice}")
if name:
    st.write(f"Hello,{name}")
data={
    "name":["john","jane","jake","Jill"],
    "Age":[28,24,35,40],
    "City":["NY","LA","Del","Hs"]
}

df=pd.DataFrame(data)
st.write(df)
df.to_csv('sampleData.csv')
uploaded_file=st.file_uploader("chose a csv file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
