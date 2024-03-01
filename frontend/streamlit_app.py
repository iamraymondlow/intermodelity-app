# Source:Below code is provided by Streamlit and AWS

import sys
import os

# Append the parent directory of the backend directory to sys.path
project_dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ""))
sys.path.append(project_dir_path)

# Import streamlit and chatbot file
import streamlit as st
from backend import app

# Set Title for Chatbot - https://docs.streamlit.io/library/api-reference/text/st.title
st.title("Welcome to Intermodelity! How can I help you today?")

# Create a dropdown list of different LLMs for selection
model_options = [
    "Amazon Titan Text G1 - Express",
    "Amazon Titan Text G1 - Lite",
    "AI21 Labs Jurassic-2 Ultra",
    "AI21 Labs Jurassic-2 Mid",
    "Cohere Command",
    "Cohere Command Light",
    "Meta Llama 2 Chat 70B",
    "Meta Llama 2 Chat 13B",
]
selected_model = st.selectbox("Select an LLM", model_options)

# LangChain memory to the session cache - Session State - https://docs.streamlit.io/library/api-reference/session-state
if "memory" not in st.session_state:
    st.session_state.memory = app.memory(model=selected_model)

# Add the UI chat history to the session cache - Session State - https://docs.streamlit.io/library/api-reference/session-state
if (
    "chat_history" not in st.session_state
):  # check if the chat history has been created yet
    st.session_state.chat_history = []  # initialize the chat history

# Re-render the chat history (Streamlit re-runs this script to preserve previous chat messages)
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

# Enter the details for chatbot input bot
input_text = st.chat_input("Enter Chat Here!")
if input_text:
    with st.chat_message("user"):
        st.markdown(input_text)

    st.session_state.chat_history.append({"role": "user", "text": input_text})

    response = app.conversation(
        input_text=input_text, memory=st.session_state.memory, model=selected_model
    )
    chat_response, llm_conversation, input_text, model = response
    print(chat_response)
    print(llm_conversation)
    print(input_text)
    print(model)

    with st.chat_message("assistant"):
        st.markdown(chat_response)

    st.session_state.chat_history.append({"role": "assistant", "text": chat_response})
