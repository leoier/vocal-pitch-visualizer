# Vocal Pitch Visualizer

Vocal Pitch Visualizer is a tool that separates the vocals from an audio and visualize the pitch with reference frequencies of musical notes

## Requirements

1. **Python 3.8+**

2. **Install dependencies** - Install the dependencies by running ```pip install -r requirements.txt```. Key dependencies: 
 - [Spleeter](https://github.com/deezer/spleeter) is a library with pretrained models to separate the voice sources of an audio using Tensorflow.

 - [Parselmouth](https://github.com/YannickJadoul/Parselmouth) is a Python library for pitch analysis on audios.

3. **FFmpeg** - Install FFmpeg from this [link](https://ffmpeg.org/download.html)

## Usage

Run the app on CLI by
```bash
python3 main.py audio_file [-s start] [-d duration]
```
where `audio_file` is the path to the file to be visualized. Optionally, you may specify the part of the audio to be processed by giving the start time and duration (in seconds). The output will be `output.mp4`.