from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import pandas as pd
import google.generativeai as genai

# Configure the key
genai.configure(api_key=os.getenv('GOOGLE-API-KEY'))

# Create the front end
st.header('❤️‍🩹Healthcare :blue[Advisor]🩺',divider='red')
input=st.text_input('👩🏻‍⚕️Hi ! I am Your Medical Expert. Ask Me Information...')

def guide_me_on(input):
    model=genai.GenerativeModel('gemini-2.5-pro')
    if input !='':
        prompt=f'''Act as a Dietician , Health Coach , Psychaterist, Expert and address the queries , 
        questions,apprehension realted to health,fitness,disease and things related to this. 
        If any query is not related to healthcare you shouls pass the messege-'Sorry I am Healthcare AI , I cant help with This...',
        Dont Prescribe any medicine or chemical salt ,even if someone ask for medicine , just say -'I am an AI Bot , Consult a Human Doctor for Medicine consultation'.
        add emojies for personal touch. '''

        response=model.generate_content(prompt+input)
        return(response.text)
    else:
        return(st.write('Please write the Prompt'))
    
submit=st.button('Submit')
if submit:
    response=guide_me_on(input)
    st.subheader(':blue[Response]')
    st.write(response)

# Creating the sidebar
st.sidebar.subheader('-`♡´- :red[BMI Calculator]')

wt=st.sidebar.text_input('Enter Weight (kg)')
ht=st.sidebar.text_input('Enter Height (cm)')

# BMI Calciulator
st.sidebar.markdown('The BMI is :') #BMI =weight/(height/100)**2
wt_num=pd.to_numeric(wt)
ht_num=pd.to_numeric(ht)
heights=ht_num/100
bmi=wt_num/(heights)**2
st.sidebar.write(bmi)    

notes=f'''
The BMI value can be interpreated as :
* Under Weight : BMI < 18.5
* Normal Weight : 18.5 < BMI < 24.9 
* Over Weight : 25 < BMI < 29.9
* Obease : BMI > 30
'''
st.sidebar.write(notes)