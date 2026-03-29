import streamlit as st
import time

st.title("My story.")
content = """
My story: Me : Born: 13th - February - 2016 \n
Dad = *Mr.Faraz Moin* \n
Mom = *Mrs.Anam* \n
Brother = *Hamaad Ullah* \n
Me = *Yamaan Faraz* \n
When I was *3* years old, My dad bought my first ever cat, *Tillu* and she was 3 months old. And after 2 years, she became *bored*. Then, Dad Bought
A cat when i was 5 years old and when i was five years old, I was in a school named *MY Public School*. It's name was *Jack*, A male. For 3 years, 
Jack *beated* Tillu a lot. then stole Dad's *Love* for Tillu. when i was 8 years old, 28th - September - 2024, my Brother was born. Then Jack 
started crying for other *cats*. So far, we didn't found any, but then, Someone came and gave a cat on 8th - October - 2024. It's name was *Rozie*,
and she was a female. She gave *4 kittens* on 24th - December - 2024. kittens: Chinu, Pinu, Kalia and Tinu. Kalia and Tinu were sold. Then i 
started with Scratch ("It isn't a language, it is a game."), Then JavaScript ("Oh no 😨, So much Hard!I better quit.") then *Rozie* gave two 
kittens on June - 2025. Kittens: Kalia and Cacto. Kalia was an early criminal. when *Rozie*Gave 6 kittens on September - 2025 and Sadly, 1 passed away, 
then Kalia killed everyone and Ate a whole kitten. Then on September - 2025, I started *Python* ("Recommended."). on that same month, 
it was my *Brother's* birthday. on February, It was my *Birthday*. on March - 11th - 2026, Rozie gave 4 kittens Sadly, 1 passed and 3 were safe. 
and on March 28, My school teacher said "Yamaan came 1st." I am 10 years old and a 3rd class student Studying in **Meerut Public School, Main wing**. \n
*Hard Work takes time* By: ***Yamaan Faraz***
"""

with st.spinner("Loading Story..."):
    time.sleep(2)
    st.progress(100, text="Steady Hands, Almost loaded...")
    time.sleep(2)

st.success(content)

st.success("My medals...")
st.image("img_4.png", width=300, caption="YF™ Official Certification From YF Schools.")
st.toast("This is my real story. Not fake", icon="✅")
import os

# 1. Look for the main folder (AC-app-Practice)
base_dir = os.path.dirname(os.path.dirname(__file__))

# 2. Use the CORRECT spelling you just found
img_path = os.path.join(base_dir, "WIN_20260308_06_18_28_Pro.jpg")

# 3. The Shield: Show the image ONLY if the path is 100% real
if os.path.exists(img_path):
    st.title("My Brother...")
    st.image(img_path, caption="Hamaad Ullah - The Money-Casher and fun-taker all day.")
else:
    st.error("The image is still missing from the main folder! 😩")
    st.info(f"Looking for: {img_path}")
import os

# 1. Look for the main folder (AC-app-Practice)
base_dir = os.path.dirname(os.path.dirname(__file__))

# 2. Use the CORRECT spelling you just found
img_path = os.path.join(base_dir, "WIN_20260303_01_48_59_Pro.jpg")

# 3. The Shield: Show the image ONLY if the path is 100% real
if os.path.exists(img_path):
    st.title("Me...")
    st.image(img_path, caption="Yamaan Faraz - The Architect")
else:
    st.error("The image is still missing from the main folder! 😩")
    st.info(f"Looking for: {img_path}")