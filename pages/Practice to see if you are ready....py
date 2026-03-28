import streamlit as st

st.title("Hello!")
st.write("Choose an option. No AI Use.")

if 'answered_correctly' not in st.session_state:
    st.session_state['answered_correctly'] = False

st.code("What is 5x7?")
b = st.button("25")
b1 = st.button("50")
b2 = st.button("35")
if b:
    st.error("Your Answer is wrong :(")
elif b1:
    st.error("Your Answer is wrong :(")
elif b2:
    st.session_state['answered_correctly'] = True
if st.session_state['answered_correctly']:
    st.success("Your Answer is absolutely right :).")
    st.code("print('Hello, World.')")
    st.markdown("In the command line, it will print **Hello, World.**")
    st.write("Why not 'Hello, World.'? as because it is a data type which i will tell you in my course.")
    i = st.text_input(placeholder="Your name?", label="Write your name here...", key="name")
    if i:
        st.success(f"Hello, {i} .Nice to meet you!")