import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Kopi Nakula - Digital Menu",
    page_icon="☕",
    layout="centered"
)

# Styling CSS Kustom untuk Tampilan Estetik & Warna Kafe
st.markdown("""
    <style>
    .stButton>button {
        background-color: #6F4E37;
        color: white;
        border-radius: 8px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #5c3a21;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Judul Kafe dengan Sentuhan Estetik
st.title("☕ Kopi Nakula")
st.markdown("### *Tempat Ngopi Santai & Estetik*")
st.write("Silakan isi data meja Anda dan pilih menu favorit di bawah ini ya!")
st.divider()

# Form Identitas Pelanggan
col_a, col_b = st.columns(2)
with col_a:
    nama_pelanggan = st.text_input("👤 Nama Anda:")
with col_b:
    nomor_meja = st.selectbox("📍 Nomor Meja:", ["Meja 1", "Meja 2", "Meja 3", "Meja 4", "VIP 1"])

st.divider()

# Daftar Menu dan Harganya
menu_items = {
    "Nakula Palm Sugar Latte": 25000,
    "Caramel Macchiato": 32000,
    "Americano Ice": 20000,
    "Croissant Butter": 22000,
    "French Fries": 18000,
}

# Inisialisasi Keranjang Belanja
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Menampilkan Menu dengan Tampilan Bersih
st.subheader("📋 Daftar Menu Pilihan")
for item, harga in menu_items.items():
    col1, col2, col3 = st.columns([3, 2, 1])
    col1.markdown(f"**{item}**")
    # Memberi warna cokelat estetik pada harga
    col2.markdown(f"<span style='color: #8B4513; font-weight: bold;'>Rp {harga:,}</span>", unsafe_allow_html=True)
    
    if col3.button("Tambah", key=item):
        if item in st.session_state.cart:
            st.session_state.cart[item] += 1
        else:
            st.session_state.cart[item] = 1
        st.success(f"Ditambahkan!")

st.divider()

# Bagian Sidebar untuk Keranjang & Checkout yang Rapi
st.sidebar.header("🛒 Keranjang Pesanan")

if nama_pelanggan:
    st.sidebar.markdown(f"**Pemesan:** {nama_pelanggan}")
    st.sidebar.markdown(f"**Lokasi:** {nomor_meja}")
    st.sidebar.divider()

if st.session_state.cart:
    total_belanja = 0
    for item, qty in st.session_state.cart.items():
        subtotal = menu_items[item] * qty
        total_belanja += subtotal
        st.sidebar.write(f"- {item} (x{qty}) : Rp {subtotal:,}")
    
    pajak = int(total_belanja * 0.1)
    grand_total = total_belanja + pajak
    
    st.sidebar.divider()
    st.sidebar.write(f"Subtotal: Rp {total_belanja:,}")
    st.sidebar.write(f"Pajak (10%): Rp {pajak:,}")
    st.sidebar.markdown(f"### **Total: Rp {grand_total:,}**")
    
    if st.sidebar.button("Kirim Pesanan"):
        if not nama_pelanggan:
            st.sidebar.error("Mohon isi Nama Anda terlebih dahulu!")
        else:
            st.sidebar.success(f"Pesanan berhasil dikirim! 🎉")
            st.session_state.cart = {}
else:
    st.sidebar.info("Keranjang masih kosong.")