import streamlit as st

st.title("Let's test your print() skill.")

st.code("print('Hello, I am YF.')")

st.write("What will it write in the command-line? write it in the input box.")

i = st.text_input(placeholder="Answer", label="Write your Answer here...", key="1")

# Added "if i:" so it doesn't say incorrect while empty
if i:
    if i == "Hello, I am YF.":
        st.success("Your answer is correct :).")
    else:
        st.error("Your answer is incorrect :(.")

st.write("Second Question...")
st.code("Hello, I have a problem with you.")
st.write("What is used to write it in the command-line? Write it in the input box.")

i2 = st.text_input(placeholder="Answer", label="Write your Answer here...", key="2")

# Added "if i2:" so it waits for the second answer too
if i2:
    if i2 == "print('Hello, I have a problem with you.')":
        st.success("Your answer is correct :).")
        st.success("You are very good! :) I am happy with you! Good Luck:)")
        st.success("Total score = 2")
    else:
        st.error("Your answer is incorrect :(. please go to page 'Practice to see if you are ready...' and learn correctly. not happy")
        st.error("Total score = 0")