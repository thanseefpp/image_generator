import openai
import streamlit as st
import urllib.request
from PIL import Image
from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

open_ai_key = os.getenv("API_KEY")

if open_ai_key is None:
  st.error("your api key is not loaded")

openai.api_key = open_ai_key

def generate_image(user_input_text):
  response = openai.Image.create(
    prompt= user_input_text,
    n=1,
    size="512x512" #output size format in 256x256, 512x512, 1024x1024
  )
  image_url = response['data'][0]['url']
  urllib.request.urlretrieve(image_url,'image.png')
  img = Image.open("image.png")
  return img


st.title("DALL·E Image Generator - OpenAI")

#Text input for image recognition
taking_input_text = st.text_input("Type anything to get generate an image")

if st.button("Generate Image"):
  generated_image = generate_image(taking_input_text)
  st.image(generated_image)