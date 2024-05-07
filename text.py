import streamlit as st  
import speech_recognition as sr  #  library li kayna9el souwt l  text
from gtts import gTTS  # Google's text-to-speech service
from io import BytesIO  
import base64  

def text_to_speech(text, lang='en'):
    tts = gTTS(text, lang=lang)  # Uses  Google TTS service bach ykhrej speech
    bio = BytesIO()  # hadi   tsajel fiha l'audio data o ktkhabih mo2a9atan
    tts.write_to_fp(bio)  # hadi tsaft l'audio data 
    return base64.b64encode(bio.getvalue()).decode('utf-8')  # returni l'audio as base64 string

def download_link(audio, filename, text):  # hadi fonction bach tdir link ta3 download
    href = f'<a href="data:file/mp3;base64,{audio}" download="{filename}">Download {text}</a>'  # sma link
    return href  

def speech_to_text(language='en'):
    r = sr.Recognizer()  # Uses  recognizer
    with sr.Microphone() as source:  # Uses  microphone comme source ta3 souwt
        st.write("Please start speaking...")
        audio = r.listen(source)  
    try:
        text = r.recognize_google(audio, language=language)  # kt7awel ta3ref l'audio
        st.success("Speech to Text Conversion Successful:")  
        st.write(text)  
        return text  
    except sr.UnknownValueError:  # ila ma fhemch l'audio
        st.error("Sorry, could not understand audio.")  
        return ""
    except sr.RequestError as e:  # ila kan chi probleme m3a service
        st.error(f"Could not request results from Google Speech Recognition service; {e}")  
        return ""
       

st.title('Text to Speech and Speech to Text Converter')  
user_input = st.text_area("Enter the text you want to convert to speech:", "Hello, welcome to our text to speech conversion tool!")  
language = st.selectbox("Choose Language for Text to Speech:", ['en', 'ar', 'es', 'de', 'fr']) 
if st.button('Convert Text to Speech'):  
    audio_base64 = text_to_speech(user_input, lang=language)  
    st.markdown(download_link(audio_base64, 'output.mp3', 'your speech file'), unsafe_allow_html=True)  # affiche l link ta3 download

st.title('Speech to Text')  # titre ta3 speech to text
speech_language = st.selectbox("Choose Language for Speech to Text:", ['en-US', 'ar-SA', 'es-ES', 'de-DE', 'fr-FR'])  
if st.button('Start Recording'):  
    text = speech_to_text(language=speech_language)  
