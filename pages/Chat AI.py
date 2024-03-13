import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Kudos AI",
    page_icon="🤖",
    layout="wide",
)

genai.configure(api_key="AIzaSyCyGBa2I6Y_fsqXXpdk-JYK3Z5TPMM4Bgo")
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 50000,
}


def gemini_chat(message, history):
    response = chat.send_message(message)
    return response.text


model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config)
chat = model.start_chat()

st.title("Chat AI")

chat_history = st.empty()  # Empty container to hold the chat history

def update_chat_history(message, response):
    chat_history.markdown(f"**You:** {message}")
    chat_history.markdown(f"KUDOS RESPONSE - {response}")

message_input = st.text_input(label="Message Kudo", placeholder="Type your message here...")

if message_input:
    response = gemini_chat(message_input, chat_history.text)
    update_chat_history(message_input, response)
    response_area = st.text_area("Response", response, height=400)


# st.button("Generate", disabled=not message_input)  # Disable button if no message entered
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)