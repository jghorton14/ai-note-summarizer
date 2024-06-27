from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_file, output_file):
    # Load the video file
    video = VideoFileClip(input_file)
    # Extract the audio and save it as an MP3 file
    video.audio.write_audiofile(output_file, codec='mp3')

# Example usage
input_file = 'test.mp4'
output_file = 'test.mp3'
convert_mp4_to_mp3(input_file, output_file)