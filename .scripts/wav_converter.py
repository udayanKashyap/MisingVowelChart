import os
from pydub import AudioSegment

def convert_ogg_to_wav(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".ogg"):
            ogg_file_path = os.path.join(directory, filename)
            wav_file_path = os.path.join(directory, filename.replace(".ogg", ".wav"))
            
            try:
                audio = AudioSegment.from_ogg(ogg_file_path)
                audio.export(wav_file_path, format="wav")
                print(f"Converted: {filename} to {filename.replace('.ogg', '.wav')}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    convert_ogg_to_wav(current_directory)

