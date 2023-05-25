import pickle
import numpy as np
import streamlit as st



st.set_page_config(
    page_title="CardioSmart",
    page_icon="🫀",

)
st.sidebar.success("Welcome to CardioSmart!")
st.sidebar.image("CardioSmart-logo.png")

st.subheader("Halo, selamat datang di CardioSmart, Smart Peeps! :wave:")
    
st.write("---")

st.header("Apa itu CardioSmart")
st.write("##")
st.image("CardioSmart-logo.png")
st.write(
    
            """
           CardioSmart adalah aplikasi yang dirancang untuk membantu user mendeteksi kemungkinan terkena penyakit jantung berdasarkan dataset 
           dari para penderita penyakit jantung agar smart peeps bisa lebih waspada dan dapat melakukan penanganan lebih lanjut jika
           diketahui telah terkena penyakit jantung.
            """
        )
st.header("Berdasarkan apa CardioSmart mendeteksi penyakit jantung smart peeps?")
col1, col2, col3, col4 = st.columns(4)

with col1:
        st.subheader("Usia Pengguna")
        st.caption("Hal ini merupakan salah satu faktor risiko jantung berdetak sangat cepat. Semakin bertambahnya usia seseorang, semakin tinggi pula risiko mengidapnya. Risiko akan semakin tinggi terutama jika seseorang berusia di atas 60 tahun. Hal tersebut lebih mungkin karena gejala dari penyakit jantung.")

with col2:
        st.subheader("Tekanan Darah")
        st.caption("Tekanan darah yang tinggi dapat meretakkan kerak (plak) di pembuluh darah koroner. Serpihan-serpihan yang terlepas dapat menyumbat aliran darah sehingga terjadilah serangan jantung.")

with col3:
        st.subheader("Kadar Kolesterol")
        st.caption("Jika berlebih, kolesterol dapat menumpuk dalam dinding pembuluh darah dan menimbulkan suatu kondisi yang disebut sebagai aterosklerosis yakni penyempitan dan pengerasan pembuluh darah yang menjadi cikal bakal terjadinya penyakit jantung koroner")
    
with col4:
        st.subheader("Detak Jantung")
        st.caption("Faktor risiko jantung berdetak sangat cepat yang umum disebabkan oleh tekanan darah tinggi. Hal tersebut membuat atrium atau ruang atas jantung menjadi lebih besar, sehingga jantung menjadi bekerja lebih keras dibanding biasanya.")
    
st.write("---")