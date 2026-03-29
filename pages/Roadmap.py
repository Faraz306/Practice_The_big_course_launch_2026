import streamlit as st
import time

st.title("Your roadmap:")
st.toast("Course isn't available right now.", icon="😩")
with st.spinner("Loading Roadmap..."):
    time.sleep(5)
    st.progress(100, text="Loading Roadmap...")
    time.sleep(2)
st.image("img_5.png")