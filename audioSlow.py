from pydub import AudioSegment
import os
import sys
import numpy as np
from scipy.io import wavfile


def slow_down_wav(input_file, output_file, factor):
    # Load the audio file
    audio = AudioSegment.from_wav(input_file)

    # Adjust the playback speed by slowing down
    slowed_audio = audio._spawn(
        audio.raw_data, overrides={"frame_rate": int(audio.frame_rate / factor)}
    ).set_frame_rate(audio.frame_rate)

    # Export the slowed audio to a new file
    slowed_audio.export(output_file, format="wav")
    # print(f"Audio slowed down by a factor of {factor} and saved to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) <= 3:
        print("Specify root dir")
        exit(0)
    rootDir = sys.argv[1]
    initial = int(sys.argv[2])
    final = int(sys.argv[3]) + 1

    for i in range(initial, final):
        filename = "voice" + str(i) + ".wav"
        filePath = os.path.join(rootDir, filename)
        outputFile = "voice" + str(i) + "_slowed.wav"
        outputPath = os.path.join(rootDir, outputFile)
        slow_down_wav(filePath, outputPath, 1.5)
