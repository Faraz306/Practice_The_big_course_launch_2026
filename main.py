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
st.write("---")
st.subheader("The YF™ Mission for Free Python Education")
st.write("""
Welcome to the official **YF™ App**, a dedicated platform created by **Yamaan Faraz** to provide a **free Python course for beginners**. Our goal is to make 
**learning programming** accessible to everyone, with a focus on 
**Python logic**, **coding tutorials**, and **software development** without charging a single penny. Whether you are looking for a 
**Python 101 guide** or **advanced coding logic**, the YF™ portal is your 
long-term resource for growth.
""")

"https://yffirstownappcoursein2026or2027.streamlit.app/"

def send_email():
    from email.message import EmailMessage
    password = "ccug yybj hkhp ekjv"
    user_email = "farazyamaan@gmail.com"
    receiver_email = "farazyamaan@gmail.com"
    import smtplib
    def send_email():
        email_msg = EmailMessage()
        email_msg['Subject'] = ('Hello To Yamaan Faraz Course.')
        email_msg.set_content("Hello, And welcome!. Sorry, But our free course is in development. But it will be available in 2027 or 2028. until then, wish you good luck!")

        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(user_email, password)
        gmail.sendmail(user_email, receiver_email, email_msg.as_string())
        gmail.quit()