import streamlit as st

st.title("Student Information")

name = st.text_input("Enter your name")

age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100
)

learning_level=st.radio("select your learning level",("Begineer","Intermediate","Advanced"))

if learning_level=="Begineer":
    st.write("You are a beginner, keep learning!")
elif learning_level=="Intermediate":
    st.write("You are at an intermediate level, keep improving!")
else:
    st.write("You are an advanced learner, keep up the great work!")

Skill = st.selectbox(
    "Choose your skill level",
    ["Beginner", "Intermediate", "Advanced"]
)

Intersted_in_AI = st.checkbox("Yes")

if Intersted_in_AI:
    st.write("Thank you for agreeing!")

if st.button("Submit"):
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Learning Level:", learning_level)
    st.write("Skill Level:", Skill)
    st.write("Interested in AI:", Intersted_in_AI)