import streamlit as st

# 💎 BOUDIOR by Rubiela - Aesthetic Boutique Website

st.set_page_config(
    page_title="BOUDIOR by Rubiela",
    page_icon="💎",
    layout="wide"
)

# 🎨 CUSTOM AESTHETIC THEME (COLORS)
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
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 🖼️ LOGO UPLOAD (OPTIONAL)
logo = st.file_uploader("Upload your boutique logo 💖", type=["png", "jpg", "jpeg"])

if logo:
    st.image(logo, width=180)
else:
    st.markdown("<h2 style='text-align:center;'>BOUDIOR</h2>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center;'>by Rubiela</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray; font-style:italic;'>Soft elegance. Bold identity.</p>", unsafe_allow_html=True)

st.divider()

# 🛍 CATEGORIES
st.subheader("🛍 Shop Categories")
categories = ["Party Wear", "Formals", "T-Shirts", "Jewellery"]
cols = st.columns(4)
for i, cat in enumerate(categories):
    with cols[i]:
        st.button(cat)

st.divider()

# 💍 JEWELLERY SECTION
st.subheader("💍 Oxidised Jewellery Collection")
cols2 = st.columns(3)
for i in range(3):
    with cols2[i]:
        st.image("https://via.placeholder.com/250x250.png?text=BOUDIOR+Product", caption="Elegant Piece")

st.divider()

# 👗 PARTY WEAR
st.subheader("👗 Party Wear")
st.write("Luxury aesthetic party wear collection for elegant looks ✨")

st.divider()

# 🛒 ORDER FORM
st.subheader("🛒 Order / Inquiry Form")

with st.form("order_form"):
    name = st.text_input("Full Name")
    whatsapp = st.text_input("WhatsApp Number")
    product = st.text_input("Product Name")
    size = st.text_input("Size")
    address = st.text_area("Full Address")
    notes = st.text_area("Extra Notes")

    submit = st.form_submit_button("Submit Order 💖")

    if submit:
        st.success("Your order has been received 💖 We will contact you on WhatsApp soon!")

st.divider()

# 📞 FOOTER
st.markdown("<p style='text-align:center; color:gray;'>© 2026 BOUDIOR by Rubiela | All Rights Reserved</p>", unsafe_allow_html=True)
