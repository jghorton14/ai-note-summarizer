# AI Note Summarizer

Uses Moviepy, whisper, and llama3 to convert mp4 files to summarize text to meeting meetings.

```
python3 -m venv 

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
python3 text-summarizer.py
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