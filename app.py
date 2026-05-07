import streamlit as st

# 💖 PAGE SETTINGS
st.set_page_config(
    page_title="BOUDIOR by Rubiela",
    page_icon="💎",
    layout="wide"
)

# 🎀 HEADER
st.markdown("""
    <div style='text-align:center; padding:20px;'>
        <h1 style='color:#8b0000; font-size:60px;'>BOUDIOR</h1>
        <h3>by Rubiela</h3>
        <p style='color:gray; font-style:italic;'>Soft elegance. Bold identity.</p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# 🛍 CATEGORIES
st.subheader("🛍 Shop Categories")

categories = ["Party Wear", "Formals", "T-Shirts", "Jewellery"]

cols = st.columns(4)

for i, cat in enumerate(categories):
    with cols[i]:
        st.button(cat)

st.divider()

# 💍 OXIDISED JEWELLERY
st.subheader("💍 Oxidised Jewellery Collection")

cols2 = st.columns(3)

for i in range(3):
    with cols2[i]:
        st.image(
            "https://via.placeholder.com/250x250.png?text=BOUDIOR+Product",
            caption="Elegant Piece"
        )

st.divider()

# 👗 PARTY WEAR SECTION
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
st.markdown("""
    <div style='text-align:center; color:gray; padding:10px;'>
        © 2026 BOUDIOR by Rubiela | All Rights Reserved
    </div>
""", unsafe_allow_html=True)
