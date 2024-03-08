import sys
import os

project_dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ""))
sys.path.append(project_dir_path)

import streamlit as st
from backend import app
from backend.app import model_parameters

# Set Title for Chatbot - https://docs.streamlit.io/library/api-reference/text/st.title
st.title("Welcome to Intermodelity! How can I help you today?")

# Create a dropdown list of different LLMs for selection
model_options = model_parameters.keys()
selected_model = st.selectbox("Select a Large Language Model", model_options, key=0)

# Define a button to refresh chat and clear all past conversations
if st.button("New Chat"):
    # Reinitialise chat history and memory
    st.session_state.chat_history = []

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

    if not st.session_state.chat_history:
        # initialise LangChain memory to session cache at the start of the conversation
        st.session_state.memory = app.memory(model=selected_model)

    st.session_state.chat_history.append({"role": "user", "text": input_text})

    response = app.conversation(
        input_text=input_text, memory=st.session_state.memory, model=selected_model
    )

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.chat_history.append({"role": "assistant", "text": response})
