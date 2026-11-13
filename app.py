import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Kopi Nakula - Digital Menu",
    page_icon="☕",
    layout="centered"
)

# Styling CSS Kustom (Warna Estetik & Rapi di HP)
st.markdown("""
    <style>
    /* Mengatur jarak pinggir layar agar pas di HP */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        padding-left: 1.2rem;
        padding-right: 1.2rem;
    }
    /* Mengubah warna tombol menjadi cokelat kopi estetik */
    .stButton>button {
        background-color: #6F4E37;
        color: white;
        border-radius: 8px;
        border: none;
        font-weight: bold;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #5c3a21;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Header Kafe
st.title("☕ Kopi Nakula")
st.divider()

# Input Data Pelanggan
nama_pelanggan = st.text_input("👤 Nama Anda:", placeholder="Ketik nama Anda di sini...")
nomor_meja = st.selectbox("📍 Nomor Meja:", ["meja 1", "meja 2", "meja 3", "meja 4", "VIP 1"])

st.divider()

# Daftar Menu dan Harga
menu_items = {
    "Palm Sugar Latte": 25000,
    "Caramel Macchiato": 32000,
    "Americano Ice": 20000,
    "Croissant Butter": 22000,
    "French Fries": 18000,
}

# Inisialisasi Keranjang Belanja
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Menampilkan Daftar Menu
st.subheader("📋 Daftar Menu")
for item, harga in menu_items.items():
    with st.container():
        st.markdown(f"**{item}**")
        col1, col2 = st.columns([2, 1])
        col1.markdown(f"<span style='color: #8B4513; font-weight: bold;'>Rp {harga:,}</span>", unsafe_allow_html=True)
        
        if col2.button("+ Tambah", key=item):
            if item in st.session_state.cart:
                st.session_state.cart[item] += 1
            else:
                st.session_state.cart[item] = 1
            st.toast(f"{item} masuk keranjang!")
        st.markdown("---")

# Bagian Keranjang & Pembayaran (Langsung di bawah menu agar mudah dilihat di HP)
st.subheader("🛒 Ringkasan Pesanan Anda")

if st.session_state.cart:
    if nama_pelanggan:
        st.info(f"**Pemesan:** {nama_pelanggan} | **Lokasi:** {nomor_meja}")
    
    total_belanja = 0
    for item, qty in st.session_state.cart.items():
        subtotal = menu_items[item] * qty
        total_belanja += subtotal
        st.write(f"• {item} **(x{qty})** — Rp {subtotal:,}")
    
    pajak = int(total_belanja * 0.1)
    grand_total = total_belanja + pajak
    
    st.divider()
    st.write(f"Subtotal: Rp {total_belanja:,}")
    st.write(f"Pajak (10%): Rp {pajak:,}")
    st.markdown(f"### Total Bayar: Rp {grand_total:,}")
    
    col_kirim, col_hapus = st.columns(2)
    with col_kirim:
        if st.button("✅ Kirim Pesanan"):
            if not nama_pelanggan:
                st.error("Isi Nama Anda terlebih dahulu ya!")
            else:
                st.success(f"Pesanan atas nama **{nama_pelanggan}** ({nomor_meja}) berhasil dikirim ke kasir! 🎉")
                st.session_state.cart = {}
    with col_hapus:
        if st.button("🗑️ Kosongkan Keranjang"):
            st.session_state.cart = {}
            st.rerun()
else:
    st.info("Keranjang masih kosong. Silakan pilih menu di atas.")