import asyncio
import edge_tts
from pydub import AudioSegment
import os

TEXT_DIR = "text"
AUDIO_DIR = "audio"

VOICE = "en-US-AriaNeural"

os.makedirs(AUDIO_DIR, exist_ok=True)

async def process_all_files():
    """Process all files asynchronously but maintain same functionality"""
    for file_name in sorted(os.listdir(TEXT_DIR)):
        if file_name.endswith(".txt"):
            text_path = os.path.join(TEXT_DIR, file_name)
            audio_path = os.path.join(
                AUDIO_DIR,
                file_name.replace(".txt", ".mp3")
            )

            with open(text_path, "r", encoding="utf-8") as f:
                text = f.read()

            print(f"Generating audio for {file_name}...")

            communicate = edge_tts.Communicate(text=text, voice=VOICE)
            temp_path = audio_path.replace(".mp3", "_temp.mp3")
            await communicate.save(temp_path)
            
            sound = AudioSegment.from_mp3(temp_path)
            faster = sound.speedup(playback_speed=1.01)
            faster.export(audio_path, format="mp3")
            
            os.remove(temp_path)

asyncio.run(process_all_files())

print("Successfully converted all text files to audio.")