import  streamlit as st

st.set_page_config(
    page_title="Kudos AI",
    page_icon="🤖",
    layout="wide",
)
st.title('Welcome to Kudos AI')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)