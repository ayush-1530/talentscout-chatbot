import streamlit as st
import google.generativeai as genai
import os
from textblob import TextBlob

# Set up Gemini API key
genai.configure(api_key=os.getenv("API_KEY"))

# Set up Streamlit app
st.set_page_config(page_title="TalentScout Hiring Chatbot", layout="wide")
st.title("🤖 TalentScout - Hiring Assistant")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_info" not in st.session_state:
    st.session_state.user_info = {}
if "questions_generated" not in st.session_state:
    st.session_state.questions_generated = False  # Track if questions are generated

# Collect user details
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

    # Generate technical questions using Gemini
    prompt = f"""
    You are a hiring assistant. Generate **3-5 technical interview questions** for each skill listed in the following tech stack:
    {', '.join(st.session_state.user_info['tech_stack'])}
    """
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    tech_questions = response.text.strip()

    # Store questions and mark them as generated
    st.session_state.tech_questions = tech_questions
    st.session_state.questions_generated = True

# Display stored messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# If questions are generated, display them
if st.session_state.questions_generated:
    st.subheader("📌 Technical Questions")
    st.markdown(st.session_state.tech_questions)

# Chat input field
user_input = st.chat_input("Ask me anything about hiring...")

if user_input:
    # Perform sentiment analysis
    sentiment = TextBlob(user_input).sentiment.polarity
    if sentiment > 0:
        sentiment_label = "😊 Positive"
    elif sentiment < 0:
        sentiment_label = "😟 Negative"
    else:
        sentiment_label = "😐 Neutral"

    # Append user input and sentiment to session
    st.session_state.messages.append({"role": "user", "content": f"{user_input} \n\n *Sentiment: {sentiment_label}*"})

    # Generate response from Gemini
    prompt = f"You are a hiring assistant. Answer professionally.\nUser: {user_input}"    
    response = model.generate_content(prompt)
    bot_reply = response.text.strip()
    
    # Append bot reply to session
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Display response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    
    # Display sentiment
    st.markdown(f"**Sentiment Analysis:** {sentiment_label}")






