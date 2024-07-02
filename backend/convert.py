from moviepy.editor import VideoFileClip
import whisper
import ssl

def convert_mp4_to_mp3(input_file, output_file):
    # Load the video file
    video = VideoFileClip("uploads/" + input_file)
    # Extract the audio and save it as an MP3 file
    video.audio.write_audiofile("uploads/" + output_file, codec='mp3')
    
    print("File successfully converted from mp4 -> mp3")
    


def mp3_to_text(filename):
    # Fix SSL context issue
    ssl._create_default_https_context = ssl._create_unverified_context

    # Load Whisper model
    model = whisper.load_model("base.en")
    print("whisper base model loaded")

    # Transcribe the audio file
    result = model.transcribe("uploads/" + filename)
    print("Finished audio transcription")

    # Get the transcribed text
    transcribed_text = result["text"]
    
    base_file_name = get_filename_without_extension(filename)

    # Save the transcribed text to a file
    with open("uploads/" + base_file_name + ".txt", "w") as file:
        file.write(transcribed_text)

    print("Transcription saved to uploads/" + base_file_name + ".txt")
    
# test.mp3 -> test
def get_filename_without_extension(filename):
    return filename.rsplit('.', 1)[0]