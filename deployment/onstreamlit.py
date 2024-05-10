# https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps
import streamlit as st
import pandas as pd
from bot import Bot

# st._config
st.set_page_config(page_icon="🚗", page_title="Urban&Mobile", layout="centered")
st.title("")
st.header("")

# -- Section: Chatbot
st.header("🤖 Chatbot")
with st.expander("[CLICK HERE TO OPEN CHATBOT]"):
    st.write("Welcome to the chatbot")
    test_user_string = st.text_input("💬")

    # if api_key and test_user_string:
    if test_user_string:
        bot = Bot(
            system="",
            user=test_user_string,
            assistant="",
        )

        response = bot.create_completion()
        st.write("URBAN & MOBILE AI Assistant:", response)
    else:
        st.warning(
            "This chatbot is for demonstration purposes only. Please enter a message to continue."
        )
