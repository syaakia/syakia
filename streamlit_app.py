import streamlit as st

st.title("kucingg ")
st.write(
    "kucingg"
)
st.image("IMG-20240515-WA0110.jpeg", width=200)

st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) ==  0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
