import streamlit as st
from transformers import pipeline
import pyttsx3

# Initialize generator
generator = pipeline("text-generation", model="gpt2")

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Streamlit UI
st.set_page_config(page_title="Text Generator", layout="centered")
st.title("📝 GPT-2 Text Generator")

# User input
prompt = st.text_input("Enter your prompt", value="Once upon a time")
max_len = st.slider("Max words to generate", 20, 300, 100)

# Generate button
if st.button("Generate"):
    with st.spinner("Generating..."):
        result = generator(prompt, max_length=max_len, num_return_sequences=1)
        output_text = result[0]['generated_text']
        st.subheader("🔍 Generated Text")
        st.write(output_text)

        # Text-to-speech
        if st.button("🔊 Speak"):
            speak(output_text)

        # Download option
        st.download_button("📥 Download Text", output_text, file_name="generated_text.txt")
