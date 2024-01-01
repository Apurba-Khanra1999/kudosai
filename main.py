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
genai.configure(api_key="AIzaSyCyGBa2I6Y_fsqXXpdk-JYK3Z5TPMM4Bgo")
model = genai.GenerativeModel("gemini-pro-vision")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "bmp"])



uploaded_text = st.text_input('What to do with the image?')

if uploaded_file is not None:
    img = PIL.Image.open(uploaded_file)
    # Create columns for layout
    col1, col2 = st.columns(2)

    # Display image in left column
    with col1:
        st.image(img, use_column_width=True)

    # Generate content based on image
    if st.button("Describe Image"):
        with st.spinner("Generating content..."):
            response = model.generate_content([uploaded_text,img], stream=True)
            response.resolve()
        # Display generated text in right column
        with col2:
            st.write(response.text)
else:
    st.write("Please upload an image to get the detailed description of the image")