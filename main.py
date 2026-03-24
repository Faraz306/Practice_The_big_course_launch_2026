import streamlit as st
import pandas as pd

# The Logic: Make the logo appear at the top of the left sidebar
# and set the width to 150 pixels so it's clean and small.
st.sidebar.image("img_3.png", width=150)
# 1. THE INITIALIZATION: This creates the "Short-Term Memory"
if 'clicked' not in st.session_state:
    st.session_state['clicked'] = False

df = pd.read_csv("data.csv")
st.title("Yamaan Faraz's app")
st.write("A place for python developers...")
# db = pd.read_csv("data.csv") # Ensure your CSV exists!

st.title("For Companies")

# 2. THE TRIGGER: This button flips the memory to "True"
if st.button("Login", key="1"):
    st.session_state['clicked'] = True

# 3. THE PERSISTENCE: This keeps the boxes visible as long as 'clicked' is True
if st.session_state['clicked']:
    email = st.text_input("Email", key="10")
    password = st.text_input("Password", type="password", key="20")

    if st.button("Submit Login", key="2"):
        st.success("Login Successful")
        st.write(f"Logged in as: {email}")
        for image in df["Picture"][:1]:
            st.image(image, width=50)
            st.success("Great developers from Python")
        # Here is where you would check 'email' against your 'db'
st.title("For Developers")

# 2. THE TRIGGER: This button flips the memory to "True"
if st.button("Login", key="3"):
    st.session_state['clicked'] = True

# 3. THE PERSISTENCE: This keeps the boxes visible as long as 'clicked' is True
if st.session_state['clicked']:
    email = st.text_input("Email", key="30")
    password = st.text_input("Password", type="password", key="40")

    if st.button("Submit Login", key="50"):
        st.success("Login Successful")
        st.write(f"Logged in as: {email}")
        for image in df["Picture"][2:]:
            st.image(image, width=50)
            st.success("Professional companies")
for image in df["Picture"]:
    st.image(image, width=50)