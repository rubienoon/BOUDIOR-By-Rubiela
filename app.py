import streamlit as st
import datetime
import csv
import os

# 💎 BOUDIOR by Rubiela - FINAL PRO BUSINESS VERSION

st.set_page_config(page_title="BOUDIOR by Rubiela", page_icon="💎", layout="wide")

# 📦 FILE STORAGE (simple database)
FILE = "orders.csv"

if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "WhatsApp", "Product", "Size", "Address", "Time"])

# 📦 SESSION
if "orders" not in st.session_state:
    st.session_state.orders = []

# 🎨 STYLE
st.markdown("""
<style>
.main {
    background-color: #fff7f7;
}
h1, h2, h3 {
    color: #8b0000;
}
.stButton button {
    background-color: #8b0000;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# 🧭 NAVIGATION
page = st.sidebar.radio("BOUDIOR MENU", ["Home", "Shop", "Order", "Admin"])

# 🏠 HOME
if page == "Home":
    st.title("💎 BOUDIOR by Rubiela")
    st.write("Luxury Boutique • Soft Elegance • Bold Identity")
    st.image("https://via.placeholder.com/1000x300.png?text=BOUDIOR+LUXURY+STORE")

# 🛍 SHOP
elif page == "Shop":
    st.header("🛍 Collection")

    st.subheader("Categories")
    st.write("Party Wear | Formals | T-Shirts | Oxidised Jewellery")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://via.placeholder.com/250")
        st.write("Party Wear Dress 💃")

    with col2:
        st.image("https://via.placeholder.com/250")
        st.write("Formal Wear 🤍")

    with col3:
        st.image("https://via.placeholder.com/250")
        st.write("Jewellery 💍")

# 🛒 ORDER SYSTEM
elif page == "Order":
    st.header("🛒 Place Your Order")

    with st.form("order_form"):
        name = st.text_input("Full Name")
        whatsapp = st.text_input("WhatsApp Number")
        product = st.text_input("Product Name")
        size = st.text_input("Size")
        address = st.text_area("Full Address")

        submit = st.form_submit_button("Confirm Order 💖")

        if submit:
            time = str(datetime.datetime.now())

            # SAVE TO CSV (REAL DATABASE)
            with open(FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([name, whatsapp, product, size, address, time])

            # STORE IN SESSION
            st.session_state.orders.append({
                "name": name,
                "whatsapp": whatsapp,
                "product": product,
                "size": size,
                "address": address,
                "time": time
            })

            # WhatsApp message link
            msg = f"Hello BOUDIOR, I want to order:\nProduct: {product}\nName: {name}\nSize: {size}\nAddress: {address}"
            wa_link = f"https://wa.me/923000000000?text={msg}"

            st.success("Order placed successfully 💖")
            st.markdown(f"👉 Send WhatsApp confirmation: [Click Here]({wa_link})")

# 🔐 ADMIN PANEL
elif page == "Admin":
    st.header("🔐 Admin Dashboard")

    password = st.text_input("Enter Admin Password", type="password")

    if password == "BOUDIOR2026":
        st.success("Welcome Admin 💼")

        st.subheader("📦 Live Orders (CSV Database)")

        try:
            with open(FILE, "r") as f:
                reader = csv.reader(f)
                data = list(reader)

            for row in data[1:]:
                st.write(row)
        except:
            st.warning("No orders found")

    else:
        st.info("Enter password to view dashboard")

# 📞 FOOTER
st.divider()
st.markdown("<p style='text-align:center;color:gray;'>© 2026 BOUDIOR by Rubiela | FINAL PRO BUSINESS SYSTEM</p>", unsafe_allow_html=True)
