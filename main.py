import streamlit as st
import time
import os

# 1. Professional Page Config
st.set_page_config(page_title="VIP Access Portal", page_icon="💎", layout="centered")

# 2. Professional CSS (Dark Mode + Logo Pop-up)
st.markdown("""
    <style>
    /* Sleek Dark Mode Background */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* Logo Pop-up Animation */
    @keyframes popup {
        0% { transform: scale(0.5); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
        animation: popup 0.8s ease-out;
    }
    
    /* Premium Button Style */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #FF4B2B, #FF416C);
        color: white;
        border-radius: 30px;
        width: 100%;
        height: 3.5em;
        font-weight: bold;
        font-size: 20px;
        border: none;
        box-shadow: 0 4px 15px rgba(255, 75, 43, 0.4);
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 75, 43, 0.6);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Logo Display (Pop-up effect)
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
files = os.listdir('.')
images = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
if images:
    # This automatically finds your logo file in the repository
    st.image(images[0], width=180)
st.markdown('</div>', unsafe_allow_html=True)

# 4. Title and Content
st.markdown("<h1 style='text-align: center; color: white;'>👑 PREMIUM MASTERCLASS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Secure your spot to unlock the exclusive content.</p>", unsafe_allow_html=True)

# 5. Payment Logic
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.write("---")
    st.link_button("🚀 UNLOCK INSTANT ACCESS - $5", "https://www.paypal.com")
    
    if st.button("✅ I HAVE PAID (CLICK TO VERIFY)"):
        with st.spinner('Verifying secure payment...'):
            time.sleep(2)
        st.session_state.authenticated = True
        st.rerun()
else:
    # SUCCESS STATE
    st.balloons()
    st.success("Payment Verified! Enjoy the video.")
    
    # YOUR ACTUAL YOUTUBE VIDEO
    st.video("https://youtu.be/-Rkr99dnCrY?si=s-3CbRNXhY5xYdFE")
    
    st.markdown("### 📝 Next Steps")
    st.write("Thanks for watching! Stay tuned for more exclusive drops from Funnyjac Tv.")
    # --- INSTALL APP SECTION ---
st.markdown("---")
with st.expander("📲 Install this as an App on your Phone"):
    st.write("To have this Masterclass on your home screen like WhatsApp:")
    st.markdown("""
    1. **Android:** Tap the **three dots (⋮)** in the top right of Chrome and select **'Add to Home Screen'**.
    2. **iPhone:** Tap the **Share icon** (square with an arrow) and select **'Add to Home Screen'**.
    """)
    st.info("Your logo will appear on your phone just like a regular app! 🚀")

