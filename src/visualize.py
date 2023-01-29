import subprocess
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from frequency import PitchFrequency


def draw_baseline():
    freqs = PitchFrequency().get_freq()
    major = [0, 2, 4, 5, 7, 9, 11]
    for i in range(len(freqs)):
        plt.axline((0, freqs[i]), (1, freqs[i]), linewidth=1, linestyle = '-' \
            if (i % 12) in major else '--')


def draw_pitch(pitch):
    # Extract selected pitch contour, and
    # replace unvoiced samples by NaN 
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values==0] = np.nan
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=5, color='w')
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=2)
    y_min = np.nanmin(pitch_values)
    y_max = np.nanmax(pitch_values)
    plt.ylim(y_min, y_max)
    plt.grid(axis='y')
    plt.ylabel('fundamental frequency [Hz]')
    return y_min, y_max


def pitch_visualize(pitch, audio_file):
    
    fig = plt.figure()
    draw_baseline()
    draw_pitch(pitch)

    prevLine = None

    def update(frame):
        nonlocal prevLine
        if prevLine is not None:
            prevLine.remove()
        prevLine = plt.axvline(frame, color='r')
        plt.xlim(left=frame-1, right=frame+1)

    moving_axis = animation.FuncAnimation(fig, update, 
                                          frames=np.linspace(pitch.xmin, pitch.xmax, 500),
                                          interval=pitch.duration/500*1000)

    # add the input soundtrack to output
    moving_axis.save('temp.mp4', writer='ffmpeg')
    input_video = 'temp.mp4'
    output_video = 'output.mp4'

    remix = ["ffmpeg", "-i", input_video, "-i", audio_file, \
            "-c:v", "copy", "-c:a", "aac", "-strict", "experimental",\
             output_video]

    subprocess.run(remix)
    subprocess.run(["rm", "temp.mp4"])
