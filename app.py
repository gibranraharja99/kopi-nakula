import streamlit as st

st.title("☕ Kopi Nakula")
st.write("Selamat datang! Silakan pilih menu di bawah ini ya:")

menu_items = {
    "Nakula Palm Sugar Latte": 25000,
    "Croissant Butter": 22000
}

for item, harga in menu_items.items():
    st.write(f"- {item} : Rp {harga:,}")
