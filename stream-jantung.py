import pickle
import numpy as np
import streamlit as st

#load save model
model = pickle.load(open("penyakit_jantung.sav",'rb'))

#judul web
st.title("Prediksi Penyakit Jantung")
col1,col2,col3 = st.columns(3)

with col1:
    age = st.number_input('Umur : ')
    sex = st.number_input('Jenis Kelamin : ')
    cp = st.number_input('chest pain : ')
    trestbps = st.number_input('trestbps : ')
with col2:
    chol = st.number_input('kolesterol : ')
    fbs = st.number_input('gula darah : ')
    restecg = st.number_input('restecg : ')
    thalach = st.number_input('detak jantung maksimum : ')
with col3:
    exang = st.number_input('induksi angina : ')
    oldpeak = st.number_input('ST depression : ')
    slope = st.number_input('slope : ')
    ca = st.number_input('Nilai ca : ')
    thal = st.number_input('Nilai thal : ')

#for prediction

heart_diagnosis = ''

if st.button('Prediksi Penyakit Jantung'):
    heart_prediction = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    if(heart_prediction[0]==1):
        heart_diagnosis = 'Kena Jantung'
    else:
        heart_diagnosis = 'A m a n'
st.success(heart_diagnosis)
