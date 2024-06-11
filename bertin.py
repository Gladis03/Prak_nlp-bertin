import streamlit as st
import stanza

# Inisialisasi model NER untuk Bahasa Indonesia
stanza.download('id')
nlp = stanza.Pipeline('id', processors='tokenize,ner')

# Judul aplikasi
st.title("Implementasi Named Entity Recognition (NER) dengan Bahasa Indonesia")

# Input teks dari pengguna
user_input = st.text_area("Masukkan teks dalam Bahasa Indonesia:", "Jakarta adalah ibu kota dari negara Indonesia.")

# Analisis teks menggunakan model NER
if st.button("Analisis Teks"):
    doc = nlp(user_input)
    
    # Menampilkan hasil NER
    st.write("Hasil Named Entity Recognition (NER):")
    for sentence in doc.sentences:
        for entity in sentence.ents:
            st.write(f"Entity: {entity.text}, Tipe: {entity.type}")

# Contoh teks
st.sidebar.subheader("Contoh Teks")
if st.sidebar.button("Contoh 1"):
    st.write("Contoh Teks 1:")
    example_text = "Presiden Joko Widodo akan mengunjungi kota Bandung pada hari Jumat."
    st.text_area("Masukkan teks dalam Bahasa Indonesia:", example
