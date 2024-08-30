import streamlit as st
import random


names = [
        "Jayesh", "Kushal", "Wilfred", "Ishir", "Hamza", "Prathik", "Hrishikesh"
]

page_element = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://wallpapercave.com/wp/wp3589963.jpg");
    background-size: cover;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
[data-testid="stToolbar"] {
    right: 2rem;
    background-image: url("");
    background-size: cover;
}
</style>
"""
st.markdown(page_element, unsafe_allow_html=True)


questions = [
    "What's your earliest memory of Anam?",
    "Can you share a funny story involving Anam?",
    "Describe a time when Anam helped you through a difficult situation.",
    "What's the most exciting adventure you've had with Anam?",
    "Tell us about a valuable life lesson you learned from Anam.",
    "Share a memory of a celebration or special occasion you enjoyed with Anam.",
    "What's a quirky habit or trait of Anam's that always makes you smile?",
    "Describe a moment when Anam surprised you in a positive way.",
    "Tell us about a tradition you and Anam started together.",
    "Share a memory of a time when you and Anam overcame a challenge together.",
    "What's the most meaningful conversation you've had with Anam?",
    "Describe a small, everyday moment with Anam that you cherish.",
    "Tell us about a skill or hobby that Anam introduced you to.",
    "Share a memory of a trip or outing you took with Anam.",
    "What's something Anam taught you that you'll never forget?"
]

def get_random_prompt():
    name = random.choice(names)
    question = random.choice(questions)
    return name, question


st.title("Memories Game")


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Generate", use_container_width=True):
        name, question = get_random_prompt()
        st.markdown(f"### {name}'s Memory of Anam")
        st.write(f"**Prompt:** *{question}*")
