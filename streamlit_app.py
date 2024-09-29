import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyC2-BBaX3ZxXqg9ztj0_2m_17p-TQ-4S0A")

model=genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input,image_data,prompt):
    response=model.generate_content([input,image_data[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {'mime_type':uploaded_file.type,
             'data':bytes_data
            }

        ]
        return image_parts
    else:
        raise FileNotFoundError("No File was uploaded")
st.set_page_config(page_title="Invoice_generator")
st.sidebar.header("Robobill")
st.sidebar.write("Made by Sarah")
st.sidebar.write("Powered by google gemini ai")
st.header("Robobill")
st.subheader("Made by IEEE WIE")
st.subheader("Manage your expenses")
input=st.text_input("What do you want me to do?",key="input")
uploaded_file=st.file_uploader("Choose an image",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

submit=st.button("Submit")

input_prompt="""
Yo are an expert in solving integration problems in calculus.We are going to upload an image of an maths problem and you will have to answer any type of questions that the user asks you.
You have to greet the user first.Make sure to keep the fonts uniform and give the solution step-by-step.At the end,make sure to repeat the name of out app "Robobill
and ask the user to use it again
"""

if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("Here's what you need to know!")
    st.write(response)
