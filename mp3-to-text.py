import whisper
import ssl

# Fix SSL context issue
ssl._create_default_https_context = ssl._create_unverified_context

# Load Whisper model
model = whisper.load_model("medium")

# Transcribe the audio file
result = model.transcribe("test.mp3")

# Get the transcribed text
transcribed_text = result["text"]

# Save the transcribed text to a file
with open("test.txt", "w") as file:
    file.write(transcribed_text)

print("Transcription saved to test.txt")