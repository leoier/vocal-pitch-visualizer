import argparse
import os
from spleeter.separator import Separator
from parselmouth import Sound
from src.visualize import pitch_visualize

parser = argparse.ArgumentParser(description='Split the vocal from the \
                                    input audio and visulize the pitch')
parser.add_argument('filename', metavar='filename',
                    help='filename of the input file')
parser.add_argument('-s', '--start', metavar='offset', type=int, default=0, 
                    help='start time of the audio to be processed')
parser.add_argument('-d', '--duration', metavar='duration', type=int, default=600.0,
                    help='duration of the audio to be processed')
parser.add_argument('-st', '--stems', metavar='stems', type=int, default=2,
                    help='number of stems to be separated, \
                        2: Vocals (singing voice) / accompaniment,\
                        4: Vocals / drums / bass / other\
                        5: Vocals / drums / bass / piano / other')

args = parser.parse_args()

audio_file = args.filename
if not os.path.isfile(audio_file):
    raise Exception('File not found')

accepted_stems = [2, 4, 5]
if not args.stems in accepted_stems:
    raise Exception('Please set the number of stems among 2, 4, and 5')

separator = Separator(f'spleeter:{args.stems}stems')
print(f'Separating {audio_file} into {args.stems} stems')
separator.separate_to_file(audio_file, './output', offset=args.start, duration=args.duration)
vocal_file = f'./output/{audio_file.split(".")[0]}/vocals.wav'
print('Separation Completed')
snd = Sound(vocal_file)
pitch = snd.to_pitch()
pitch_visualize(pitch, vocal_file)
print('output.mp4 created')