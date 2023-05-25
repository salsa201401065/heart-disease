import pickle
import numpy as np
import streamlit as st



st.set_page_config(
    page_title="CardioSmart",
    page_icon="🫀",

)
st.sidebar.success("Welcome to CardioSmart!")
st.sidebar.image("CardioSmart-logo.png")
# load save model
model = pickle.load(open('penyakit-jantung.sav','rb'))

# judul web
st.title('Prediksi Kesehatan Jantung')

col1, col2, col3, col4 = st.columns(4)

with col1:
    age = st.number_input('Umur')
with col2:
    trestbps = st.number_input('Tekanan Darah')
with col3:
    chol = st.number_input('Kolestrol')
with col4:
    thalach = st.number_input('Detak Jantung')
    st.caption("Hitung detak jantung Anda per/menit gunakan stopwatch sebagai alat bantu")

# code for prediction
heart_diagnosis =''

# membuat tombol prediksi
if st.button('Prediksi Kesehatan Jantung'):
    heart_prediction = model.predict([[age, trestbps, chol, thalach]])

    if (heart_prediction[0]==1):
        heart_diagnosis = 'Anda Terkena Penyakit Jantung'
    else:
        heart_diagnosis = 'Anda Tidak Terkena Penyakit Jantung'
st.success(heart_diagnosis)


