# AI Note Summarizer

Uses Moviepy, whisper, and llama3 to convert mp4 files to summarize text to meeting meetings.


## Create test mp4
```
yt-dlp -f mp4 "https://www.youtube.com/watch?v=9-GRzu6zbS0" -o test.mp4
```

## Install ffmpeg
Linux
```
sudo apt install ffmpeg

```

Mac
```
brew install ffmpeg
```


## Configure Ollama to for llama3
Download and configure ollama to use llama3:

https://ollama.com/

```
ollama pull llama3
ollama run llama3
```

## Configure Python

```
python3 -m venv myenv

source myenv/bin/activate

pip install -r requirements.txt
```

1) convert mp4 -> mp3
```
python3 mp4-to-mp3.py
```

2) convert mp3 -> text
```
python3 mp3-to-text.py
```

3) summarize text
```
python3 text-summarizer.py > OUTPUT.md
```

This will produce an output like this:

    summarized text:  Here are the meeting minutes summarized:

    **Meeting Summary:**

    This meeting was a self-recorded video discussion by Michael about building a car out of electric scooters. He presented his idea, demonstrated a prototype, and highlighted safety features. The attendees were not specified.

    **Action Items:**

    1. Develop a more advanced controller to individually communicate with each scooter's throttle.
    2. Learn Python programming to connect the Arduino to the scooters.

    **Discussion Points:**

    * Feasibility of building a car out of electric scooters
    * Potential legal implications of modifying public rental scooters
    * Safety features and considerations for this project

    **Next Steps:** None specified, but it appears that Michael is committed to pursuing this idea further and exploring ways to make it more practical and safe.

    Note: The meeting minutes are based on the provided transcript and may contain errors or inaccuracies.

    
docker run -d -p 9099:9099 --add-host=host.docker.internal:host-gateway -v pipelines:/app/pipelines --name pipelines --restart always ghcr.io/open-webui/pipelines:main


```
export WEBUI_AUTH=True
pip install open-webui
open-webui serve
```

## Docker 

Pull Ollama
```
docker pull ollama/ollama
```

Start Ollama with CPU only on port 11434
```
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

Run llama3 model
```
docker exec -it ollama ollama run llama3
```



Ensure ollama is up and running...
```
http://localhost:11434/
```

docker-compose build
docker-compose up


## Local Development

Start the backend flask app:
```
cd backend
pip install -r requirements.txt
python3 app.py
``` 

### Process File Endpoint:
```
curl -X POST http://127.0.0.1:5001/process-file
```