import streamlit as st
import time

st.title("My Apps.")
st.write("This isn't my only app. instead, i have more apps. evidence")
with st.spinner("Showing apps..."):
    time.sleep(1)
    my_bar = st.progress(0, text="Loading YF Portfolio...")
    for percent_complete in range(100):
        time.sleep(0.02)  # This makes it smooth
        my_bar.progress(percent_complete + 1, text="Almost loaded...")
st.image("img_11.png")
st.toast("My profile and apps.", icon="💹")
st.snow()
st.balloons()
st.image("img_3.png", width=300)
st.image("img_4.png", width=200)
st.badge(label="Yf Certification 🥇🥈🥉YF Headquarters Official.🥉🏅🏆")
st.image("img_5.png", width=200)