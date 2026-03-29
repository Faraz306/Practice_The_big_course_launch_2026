import streamlit as st

student_name = st.text_input("Enter your name for the Medal:")

if st.button("🏅 EARN MEDAL"):
    if student_name:
        # THE REPAIR: Added 'f.flush()' to force the write!
        with open("YF_schools.txt", "a") as f:
            f.writelines(f"{student_name}\n")
            f.flush() # This forces Python to let go of the text!

        st.header(f"✨ {student_name} ✨")
        st.image("img_4.png", width=300)
        st.write("Complete course, get medal. Not available right now.")
        st.snow()
        st.balloons()
        st.success("Log Updated: Your victory is recorded.")
        st.toast("Practice on the page 'Practice to see if you are ready...'", icon="💹")