import base64

import streamlit as st
from PIL import Image

st.title('hello world')
st.write('main')
st.sidebar.title('Боковая панель')

# img = Image.open('background.jpg')
# st.image(img, width=500)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('background.jpg')