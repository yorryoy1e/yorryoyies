import streamlit as st

st.title("Selamat Datang di Web Informatika")
st.write(
    "ngodingseru bersama Yorry Galvina"
)
st.image("https://github.com/yorryoy1e/yorryoyies/blob/main/355128B9-CEA5-408C-986F-3DB80FB97D38.jpeg", width=200)



st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
