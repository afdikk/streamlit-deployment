import streamlit as st
import pickle
import numpy as np

# Load Model
try:
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("File model.pkl tidak ditemukan!")

st.title("Aplikasi Prediksi Pembelian 🛒")
st.write("Aplikasi ini memprediksi apakah pelanggan akan membeli produk berdasarkan Umur dan Gaji.")

# Input Form
st.header("Masukkan Data Pelanggan")
umur = st.number_input("Masukkan Umur", min_value=0, max_value=100, value=25)
gaji = st.number_input("Masukkan Gaji (Rupiah)", min_value=0, value=5000000, step=500000)

# Tombol Prediksi
if st.button("Prediksi Sekarang"):
    # Siapkan data (Format harus sama persis saat training: Umur lalu Gaji)
    data_input = np.array([[umur, gaji]])
    
    # Lakukan prediksi
    hasil_prediksi = model.predict(data_input)
    
    # Tampilkan hasil yang ramah pengguna
    if hasil_prediksi[0] == 1:
        st.success("Prediksi: Pelanggan KEMUNGKINAN BESAR akan membeli produk! 🎯")
        st.balloons()
    else:
        st.warning("Prediksi: Pelanggan KEMUNGKINAN KECIL membeli produk. 📉")