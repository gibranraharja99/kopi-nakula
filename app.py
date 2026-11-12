import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Kopi Nakula - Digital Menu",
    page_icon="☕",
    layout="centered"
)

# Judul Kafe
st.title("☕ Kopi Nakula")
st.write("Silakan masukkan info meja Anda dan pilih menu favorit di bawah ini!")
st.divider()

# Form Identitas Pelanggan (Nomor Meja)
col_a, col_b = st.columns(2)
with col_a:
    nama_pelanggan = st.text_input("Nama Anda:")
with col_b:
    nomor_meja = st.selectbox("Nomor Meja:", ["Meja 1", "Meja 2", "Meja 3", "Meja 4", "VIP 1"])

st.divider()

# Daftar Menu dan Harganya dalam bentuk Dictionary Python
menu_items = {
    "Nakula Palm Sugar Latte": 25000,
    "Caramel Macchiato": 32000,
    "Americano Ice": 20000,
    "Croissant Butter": 22000,
    "French Fries": 18000,
}

# Inisialisasi Keranjang Belanja di Memori Python
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Menampilkan Menu Menggunakan Looping Python
st.subheader("📋 Daftar Menu")
for item, harga in menu_items.items():
    col1, col2, col3 = st.columns([3, 2, 1])
    col1.markdown(f"**{item}**")
    col2.text(f"Rp {harga:,}")
    
    # Tombol Tambah ke Keranjang
    if col3.button("Tambah", key=item):
        if item in st.session_state.cart:
            st.session_state.cart[item] += 1
        else:
            st.session_state.cart[item] = 1
        st.success(f"Berhasil menambahkan {item}!")

st.divider()

# Bagian Sidebar untuk Keranjang & Checkout
st.sidebar.header("🛒 Keranjang Pesanan")

if nama_pelanggan:
    st.sidebar.write(f"👤 Pemesan: **{nama_pelanggan}**")
    st.sidebar.write(f"📍 Lokasi: **{nomor_meja}**")
    st.sidebar.divider()

if st.session_state.cart:
    total_belanja = 0
    for item, qty in st.session_state.cart.items():
        subtotal = menu_items[item] * qty
        total_belanja += subtotal
        st.sidebar.write(f"- {item} (x{qty}) : Rp {subtotal:,}")
    
    # Hitung Pajak 10%
    pajak = int(total_belanja * 0.1)
    grand_total = total_belanja + pajak
    
    st.sidebar.divider()
    st.sidebar.write(f"Subtotal: Rp {total_belanja:,}")
    st.sidebar.write(f"Pajak (10%): Rp {pajak:,}")
    st.sidebar.markdown(f"### **Total: Rp {grand_total:,}**")
    
    # Tombol Checkout
    if st.sidebar.button("Kirim Pesanan ke Kasir"):
        if not nama_pelanggan:
            st.sidebar.error("Mohon isi Nama Anda terlebih dahulu di halaman utama!")
        else:
            st.sidebar.success(f"Pesanan untuk {nama_pelanggan} di {nomor_meja} berhasil dikirim! 🎉")
            st.session_state.cart = {}
else:
    st.sidebar.info("Keranjang Anda masih kosong.")