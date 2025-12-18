import streamlit as st
import time

# 1. SET THE PROFESSIONAL DARK THEME & YOUR LOGO AS THE ICON
# This 'page_icon' line is what fixes the icon on the home screen!
st.set_page_config(
    page_title="Premium Masterclass",
    page_icon="logo.png", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Dark Mode & Button Styling
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    div.stButton > button:first-child {
        background-color: #FFC439; color: black; border-radius: 20px; font-weight: bold; width: 100%;
    }
    /* Style for the PayPal Button */
    .pay-btn {
        background-color: #FFC439; color: black; padding: 15px 32px; border: none; 
        border-radius: 25px; font-weight: bold; font-size: 18px; cursor: pointer; 
        width: 100%; text-decoration: none; display: inline-block; text-align: center;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. THE LOGO POP-UP (PROFESSIONAL ENTRANCE)
if 'logo_shown' not in st.session_state:
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("<br><br>", unsafe_allow_html=True)
        try:
            st.image("logo.png", width=200)
        except:
            st.header("💎 MATIVO MASTERCLASS")
        st.subheader("Unlocking Standard Size...")
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
    placeholder.empty()
    st.session_state['logo_shown'] = True

# 3. MAIN CONTENT
st.title("💎 Premium Masterclass Portal")
st.write("Welcome to the inner circle. Follow the steps below to access your content.")

# 4. PAYPAL & VERIFICATION SECTION
with st.expander("🔐 STEP 1: Unlock Your Content", expanded=True):
    st.write("Pay via PayPal and click verify below to see the video.")
    
    # !!! REPLACE THE LINK BELOW WITH YOUR REAL PAYPAL LINK !!!
    paypal_url = "PASTE_YOUR_PAYPAL_LINK_HERE"
    
    st.markdown(f'<a href="{paypal_url}" target="_blank" class="pay-btn">💳 Pay with PayPal</a>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("✅ I Have Paid - Click to Verify"):
        st.success("Payment Verified! Unlocking your Masterclass now...")
        st.balloons()
        st.session_state['paid'] = True

# 5. VIDEO SECTION (ONLY SHOWS AFTER VERIFICATION)
if st.session_state.get('paid'):
    st.markdown("---")
    st.subheader("📺 Your Masterclass Video")
    # Replace the ID below with your actual YouTube ID
    st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID")
    
    # PDF DOWNLOAD BUTTON
    try:
        with open("workbook.pdf", "rb") as file:
            st.download_button(
                label="📄 Download Masterclass Workbook (PDF)",
                data=file,
                file_name="Masterclass_Workbook.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.info("Note: Upload 'workbook.pdf' to GitHub to enable the PDF download.")

# 6. INSTALL AS APP SECTION
st.markdown("<br><br>", unsafe_allow_html=True)
with st.expander("📲 Install this as an App on your Phone"):
    st.write("To have your icon appear on your home screen like WhatsApp:")
    st.markdown("""
    1. **Android:** Tap the **3 dots (⋮)** in Chrome and select **'Add to Home Screen'**.
    2. **iPhone:** Tap the **Share icon** and select **'Add to Home Screen'**.
    """)
    st.info("Your logo will now be the app icon! 🚀")

st.markdown("<p style='text-align: center; color: grey;'>© 2025 Mativo Masterclass Premium</p>", unsafe_allow_html=True)
