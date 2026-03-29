import streamlit as st
import time

st.title("YF™ Schools: Test your print() skill.")

# --- QUESTION 1 ---
st.code("print('Hello, I am YF.')")
st.write("What will it write in the command-line? write it in the input box.")

i = st.text_input(placeholder="Answer", label="Write your Answer here...", key="1")

# THE REPAIR: Added 'if i:' so it only spins AFTER they type
if i:
    with st.spinner("Checking..."):
        time.sleep(1.0)

    if i == "Hello, I am YF.":
        st.success("Your answer is correct :).")
    else:
        st.error("Your answer is incorrect :(.")

st.divider()

# --- QUESTION 2 ---
st.write("### *Second Question...*")
st.code("Hello, I have a problem with you.")
st.write("What is used to write it in the command-line? Write it in the input box.")

i2 = st.text_input(placeholder="Answer", label="Write your Answer here...", key="2")

# THE REPAIR: Added 'if i2:' and fixed indentation
if i2:
    with st.spinner("Checking..."):
        time.sleep(1.5)

    if i2 == "print('Hello, I have a problem with you.')":
        st.success("Your answer is correct :).")
        st.success("You are very good! :) I am happy with you! Good Luck:)")
        st.success("Total score = 2")
        st.toast('YF™ Certification Unlocked!', icon='🏅')

        st.balloons()
        st.image("img_4.png", width=300, caption="YF™ Official Certification From YF Schools.")
        st.snow()

        with open("YF_schools.txt", "a") as f:
            f.write(f"GRADUATE: {i} | PASSED LEVEL 2\n")
        bar = st.progress(0, text="Course Progress")
        bar.progress(100, text="Successfully ready for the incoming course. checking progress...")
        st.spinner("Checking...")
        time.sleep(1.5)
        st.progress(100, text="You are special! Good Luck :)!")
    else:
        st.error("Your answer is incorrect :(. please go to page 'Practice' and learn correctly. not happy")
        st.error("Total score = 0")
        bar = st.progress(0)
        bar.progress(0, text="COMPLETE FAILURE! please learn but i think you are not ready, Bye!")
        st.toast('Failed.', icon='❌')