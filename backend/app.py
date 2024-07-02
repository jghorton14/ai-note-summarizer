from convert import convert_mp4_to_mp3, mp3_to_text
from process import process_chunks, summarize_using_llama3

from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        return jsonify({'message': 'File successfully uploaded'}), 200    
    
# TODO Pass in filename, handle if mp4 vs srt
@app.route('/process-file', methods=['POST'])
def process_file():
    
    # 1) check if passed in filename is not empty and is valid file to process (mp4, srt, etc)
    
    # 2) convert file from `format` to mp3
    convert_mp4_to_mp3("test.mp4", "test.mp3")
    
    # 3) process text 
    mp3_to_text("test.mp3")
    
    # 4) Summarize text
    summarized_chunk_arr = process_chunks("uploads/test.txt")
    combined_summary = " ".join(summarized_chunk_arr)
    sum_chunk = summarize_using_llama3(combined_summary)
    print(sum_chunk)

    return jsonify({'message': 'File successfully processed'}), 200
 
#  TODO create functionality
@app.route('/process-all-files', methods=['POST'])
def process_all_files():
    return jsonify({'message': 'File successfully uploaded'}), 200     

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
