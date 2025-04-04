import streamlit as st
import openai
import os
from textblob import TextBlob 

openai.api_key = os.getenv("API_KEY")

if openai.api_key is None:
    st.error("🚨 OpenAI API key is missing! Please set it in the .env file.")

st.set_page_config(page_title="TalentScout Hiring Chatbot", layout="wide")
st.title("🤖 TalentScout - Hiring Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_info" not in st.session_state:
    st.session_state.user_info = {}
if "questions_generated" not in st.session_state:
    st.session_state.questions_generated = False  

with st.form(key="user_form"):
    full_name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.slider("Years of Experience", 0, 20, 1)
    location = st.text_input("Current Location")
    tech_stack = st.text_area("Tech Stack (comma-separated, e.g., Python, Django, React, PostgreSQL)")

    submit = st.form_submit_button("Submit")

if submit:
    st.session_state.user_info = {
        "name": full_name,
        "email": email,
        "phone": phone,
        "experience": experience,
        "location": location,
        "tech_stack": tech_stack.split(", ")
    }
    st.success("Information submitted successfully! Generating questions...")
    prompt = f"""
    You are a hiring assistant. Generate **3-5 technical interview questions** for each skill listed in the following tech stack:
    {', '.join(st.session_state.user_info['tech_stack'])}
    
    Example:
    - Python: What are Python decorators? Explain with an example.
    - Django: How does Django handle database migrations?
    - React: What is the virtual DOM in React, and why is it used?
    """

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )

    tech_questions = response.choices[0].message.content
    st.session_state.tech_questions = tech_questions
    st.session_state.questions_generated = True

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.questions_generated:
    st.subheader("📌 Technical Questions")
    st.markdown(st.session_state.tech_questions)

user_input = st.chat_input("Ask me anything about hiring...")

if user_input:
    sentiment = TextBlob(user_input).sentiment.polarity
    if sentiment > 0:
        sentiment_label = "😊 Positive"
    elif sentiment < 0:
        sentiment_label = "😟 Negative"
    else:
        sentiment_label = "😐 Neutral"
    st.session_state.messages.append({"role": "user", "content": f"{user_input} \n\n *Sentiment: {sentiment_label}*"})
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a hiring assistant. Answer professionally."},
            {"role": "user", "content": user_input}
        ]
    )

    bot_reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.markdown(bot_reply)
 
    st.markdown(f"**Sentiment Analysis:** {sentiment_label}")

