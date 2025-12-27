import streamlit as st
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, "audio")

st.set_page_config(page_title="Announcement System", layout="centered")
st.title("Announcement System")

if not os.path.isdir(AUDIO_DIR):
    st.error("audio' folder not found.")
    st.stop()

audio_files = sorted([
    f for f in os.listdir(AUDIO_DIR)
    if f.lower().endswith(".mp3")
])

if not audio_files:
    st.error("No MP3 files found in the audio folder.")
    st.stop()

selected_award = st.selectbox(
    "Select Award to Announce",
    audio_files
)

audio_path = os.path.join(AUDIO_DIR, selected_award)

st.audio(audio_path)

st.success()