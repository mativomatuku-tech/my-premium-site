import streamlit as st
import os
import time

# 1. Pro Config
st.set_page_config(page_title="VIP Exclusive", page_icon="💎", layout="centered")

# 2. Sleek Pro Styles
st.markdown("""
    <style>
    .stApp { background-color: #0a0a0a; color: white; }
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #FF4B2B, #FF416C);
        color: white; border-radius: 25px; width: 100%; height: 3.5em;
        font-weight: bold; font-size: 20px; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Logo & Brand
all_files = os.listdir('.')
images = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
if images:
    st.image(images[0], width=180)

st.markdown("<h1 style='text-align: center;'>👑 VIP PORTAL</h1>", unsafe_allow_html=True)

# 4. Placeholder Link (We will change this to your PayPal later!)
TEMP_PAYMENT_LINK = "https://www.google.com" 

if 'paid' not in st.session_state:
    st.session_state.paid = False

if not st.session_state.paid:
    st.link_button("🚀 UNLOCK VIDEO - $5", TEMP_PAYMENT_LINK)
    st.write(" ")
    if st.button("✅ I HAVE PAID (VERIFY)"):
        with st.spinner('Verifying transaction...'):
            time.sleep(2) # Makes it look like it's actually checking!
        st.session_state.paid = True
        st.rerun()
else:
    st.balloons()
    st.success("Access Granted!")
    videos = [f for f in all_files if f.lower().endswith('.mp4')]
    if videos:
        st.video(videos[0])