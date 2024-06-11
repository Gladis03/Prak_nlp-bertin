import streamlit as st
from textblob import TextBlob

# Judul aplikasi
st.title("Aplikasi Analisis Sentimen")

# Input teks dari pengguna
user_input = st.text_area("Masukkan teks untuk analisis sentimen:")

# Tombol untuk analisis sentimen
if st.button("Analisis Sentimen"):
    if user_input:
        # Lakukan analisis sentimen
        blob = TextBlob(user_input)
        sentiment = blob.sentiment

        # Tampilkan hasil analisis
        st.write("**Polarity:**", sentiment.polarity)
        st.write("**Subjectivity:**", sentiment.subjectivity)

        # Interpretasi hasil
        if sentiment.polarity > 0:
            st.write("Sentimen: **Positif**")
        elif sentiment.polarity < 0:
            st.write("Sentimen: **Negatif**")
        else:
            st.write("Sentimen: **Netral**")
    else:
        st.write("Silakan masukkan teks untuk dianalisis.")
