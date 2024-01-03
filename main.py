# import google.generativeai as genai
# import PIL.Image
# import streamlit as st
# genai.configure(api_key="AIzaSyCyGBa2I6Y_fsqXXpdk-JYK3Z5TPMM4Bgo")
# model = genai.GenerativeModel("gemini-pro-vision")
#
# uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "bmp"])
# # img = PIL.Image.open('image.jpg')
# # response= model.generate_content(img)
# # print(response.text)
# if uploaded_file is not None:
#     img = PIL.Image.open(uploaded_file)
#     # Create columns for layout
#     col1, col2 = st.columns(2)
#
#     # Display image in left column
#     with col1:
#         st.image(img, use_column_width=True)
#
#     # Generate content based on image
#     if st.button("Describe Image"):
#         with st.spinner("Generating content..."):
#             response = model.generate_content(img)
#         # Display generated text in right column
#         with col2:
#             st.write(response.text)
# else:
#     st.write("Please upload an image to get the detailed description of the image")


# -------------------------------------------------------------------------------------------------------------

import google.generativeai as genai
import PIL.Image
import streamlit as st
import requests
from io import BytesIO

st.set_page_config(
    page_title="Kudos AI",
    page_icon="🤖",
    layout="wide",
)

genai.configure(api_key="AIzaSyCyGBa2I6Y_fsqXXpdk-JYK3Z5TPMM4Bgo")
model = genai.GenerativeModel("gemini-pro-vision")
st.markdown("<h1 style='text-align: center;'>Kudos AI 🤖</h1>", unsafe_allow_html=True)
st.subheader("Play with Image")
filecol, textcol = st.columns(2)
with filecol:
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "bmp"])
with textcol:
    st.text('Do more with the Image \neg. Write a blog based on the image...\n    What is the recipe of the food? etc.')
    uploaded_text = st.text_input('What to do with the image? (Optional)')

if uploaded_file is not None:
    img = PIL.Image.open(uploaded_file)
    # Create columns for layout
    col1, col2 = st.columns(2)

    # Display image in left column
    with col1:
        st.image(img, use_column_width=True)

    # Generate content based on image
    with col2:
        if st.button("Describe Image"):
            with st.spinner("Generating content..."):
                response = model.generate_content([uploaded_text, img], stream=True)
                response.resolve()
                st.write(response.text)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)