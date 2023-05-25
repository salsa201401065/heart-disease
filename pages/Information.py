import pickle
import numpy as np
import streamlit as st



st.set_page_config(
    page_title="CardioSmart",
    page_icon="🫀",

)
st.sidebar.success("Welcome to CardioSmart!")
st.sidebar.image("CardioSmart-logo.png")

st.subheader("Smart peeps!:wave: , kenalan yuk sama penyakit jantung!")
    
st.write("---")

st.header("Bagaimana penyakit jantung di Indonesia?")
st.write("##")
st.image("statistik.png")
st.write(
    
            """
           Berdasarkan data statistik dari Data Organisasi Kesehatan Dunia (WHO), menunjukkan terdapat 10 penyakit sebagai penyebab kematian tertinggi di Indonesia. Urutan pertama adalah stroke dengan 131,8 kasus kematian per 100 ribu penduduk. Kedua, ada jantung iskemik atau penyebab serangan jantung dengan 95,68 kasus.
Berdasarkan data Riset Kesehatan Dasar (Riskesdas) tahun 2018, angka kejadian penyakit jantung dan pembuluh darah semakin meningkat dari tahun ke tahun. Setidaknya, 15 dari 1000 orang, atau sekitar 2.784.064 individu di Indonesia menderita penyakit jantung.

            """
        )

st.header("Apa itu penyakit jantung?")
st.write("##")
st.write(
    
            """
                    Jantung adalah organ vital pada makhluk hidup, terkhusus pada manusia yang berfungsi untuk memompa darah yang membawa oksigen dan nutrisi yang siap disalurkan ke seluruh bagian tubuh. 
          Penyakit jantung adalah keadaan dimana jantung tidak dapat melaksanakan fungsinya dengan baik, sehingga kerja jantung sebagai pemompa darah dan pembawa oksigen ke seluruh tubuh terganggu. 

          Penyakit jantung bisa disebabkan oleh berbagai hal, 
          seperti sumbatan pada pembuluh darah jantung, peradangan, infeksi atau kelainan bawaan.
          
          
          Beberapa faktor eksternal yang yang menjadi penyebab seseorang menderita penyakit jantung:
            - Merokok
            - Mengonsumsi makanan dengan lemak tinggi
            - Terlalu banyak mengonsumsi minuman beralkohol
            - Gaya hidup tidak aktif / malas berolahraga
            
            """
        )
st.header("Apa saja gejela umum dari seseorang yang terkena penyakit jantung?")
col1, col2, col3, col4 = st.columns(4)

with col1:
        st.subheader("Nyeri pada dada")
        st.caption("Munculnya rasa seperti terbakar pada dada sebelah kiri. Disertai pula dengan Sesak napas, yang biasanya disertai dengan keringat dingin, rasa lemas, bahkan mengalami pingsan.")

with col2:
        st.subheader("Bengkak pada Organ")
        st.caption("Pembengkakan terjadi pada organ paru-paru dan anggota tubuh bagian bawah. Hal ini terjadi disebabkan oleh berkumpulnya cairan pada suatu titik.")

with col3:
        st.subheader("Keringat berlebih")
        st.caption("Berkeringat tidak harus di bawah terik matahari atau sedang berolahraga, namun bisa terjadi walaupun anda ada di ruangan ber-AC sekalipun.")
    
with col4:
        st.subheader("Jantung berdebar")
        st.caption("Berdebar secara tidak normal atau biasa dikenal pula dengan palpitasi.")
    
st.write("---")

st.header("Pertolongan Pertama pada Orang yang terkena Serangan Jantung")
st.write("##")
st.image("cpr.png")
