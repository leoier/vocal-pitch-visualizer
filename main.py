import argparse
import os
from spleeter.separator import Separator
from parselmouth import Sound
from visualize import pitch_visualize

parser = argparse.ArgumentParser(description='Split the vocal from the \
                                    input audio and visulize the pitch')
parser.add_argument('filename', metavar='filename',
                    help='filename of the input file')
parser.add_argument('-s', '--start', metavar='s_0', type=int, default=0, 
                    help='start time of the audio to be processed')
parser.add_argument('-d', '--duration', metavar='d', type=int, default=600.0,
                    help='duration of the audio to be processed')

args = parser.parse_args()

audio_file = args.filename
if not os.path.isfile(audio_file):
    raise Exception("File not found")

separator = Separator('spleeter:2stems')
separator.separate_to_file(audio_file, './output', offset=args.start, duration=args.duration)
vocal_file = f'./output/{audio_file.split(".")[0]}/vocals.wav'
snd = Sound(vocal_file)
pitch = snd.to_pitch()
pitch_visualize(pitch, vocal_file)
