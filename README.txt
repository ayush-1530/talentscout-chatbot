# TalentScout Hiring Assistant

## Overview
The **TalentScout Hiring Assistant** is an AI-powered chatbot designed to assist with technical hiring. It generates interview questions based on a candidate's tech stack and provides real-time interactive responses to hiring-related queries. The chatbot has been implemented using both **OpenAI (ChatGPT)** and **Google Gemini (GenAI)** models.

## Features
- 🤖 **AI-Powered Question Generation**: Generates **3-5 technical interview questions** based on the provided tech stack.
- 🗣 **Interactive Chat**: Users can ask hiring-related questions and receive AI-generated responses.
- 📊 **Sentiment Analysis**: Gauges candidate emotions during the conversation.
- 🌍 **Multilingual Support**: Detects and responds in the candidate’s preferred language.
- 🎯 **Personalized Responses**: Learns from user interactions and provides contextual replies.
- 🎨 **Enhanced UI/UX**: Custom-styled interface for a smooth and professional experience.

## Implementation
### 1️⃣ OpenAI (ChatGPT) Version
Implemented using **OpenAI's GPT-3.5-Turbo/4** model for generating interview questions and responding to candidate queries.

### 2️⃣ Google Gemini (GenAI) Version
Implemented using **Google's Gemini-Pro** model for content generation, providing an alternative AI backend.

## Installation & Setup
### Prerequisites
- Python 3.8+
- Streamlit
- OpenAI API Key (for ChatGPT version)
- Google Gemini API Key (for GenAI version)

### Installation
```sh
# Clone the repository
git clone https://github.com/yourusername/talentscout-chatbot.git
cd talentscout-chatbot

# Install dependencies
pip install -r requirements.txt
```

### Running the App
#### OpenAI Version:
```sh
export OPENAI_API_KEY="your_openai_api_key"
streamlit run app_openai.py
```

#### Google Gemini Version:
```
export GEMINI_API_KEY="your_gemini_api_key"
streamlit run app_gemini.py
```

## Usage
1. Enter candidate details in the form.
2. The AI generates interview questions based on the provided tech stack.
3. Candidates can interact with the chatbot for hiring-related queries.
4. Sentiment analysis and multilingual support enhance interactions.

## Contributing
Contributions are welcome! Feel free to fork the repo and submit pull requests.

## License
This project is licensed under the MIT License.

NOTE - As I am a student so, it is difficult for me to afford the chatgpt or gemini advance version. You can use your own API_KEY to run this project without any errors.