import csv
import pprint
import parselmouth
from parselmouth import praat
import textgrid as tg
import os

voiceDir = "MisingSentences/V1"
annoDir = "MisingSentences/An1"
outputDir = "formantData"


def main():
    sentenceCounter = 0
    for voiceFilename in os.listdir(voiceDir):
        voicePath = os.path.join(voiceDir, voiceFilename)
        if not os.path.isfile(voicePath):
            continue

        voice = parselmouth.Sound(voicePath)
        annotationPath = os.path.join(annoDir, getAnnotatedFilename(voiceFilename))
        outputFilename = voiceFilename[:-3] + "csv"
        outputPath = os.path.join(outputDir, outputFilename)
        if os.path.exists(annotationPath):
            voiceTextgrid = tg.TextGrid.fromFile(annotationPath)
            # print(voiceTextgrid[0][0])
            formantData = getFormants(voice, voiceTextgrid)
            sentenceCounter += 1
            with open(outputPath, "w", newline="") as csvfile:
                fieldnames = formantData[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(formantData)
    print("Sentences processed: " + str(sentenceCounter))


def getAnnotatedFilename(voiceFilename):
    annotationFilename = voiceFilename.replace("(", "_")
    annotationFilename = annotationFilename.replace(")", "_")
    annotationFilename = annotationFilename[:-3]
    annotationFilename += "TextGrid"
    return annotationFilename


def getFormants(sound, soundTextgrid):
    data = []

    # parameters of formant extraction
    timestep_s = 0.0025
    max_formants = 5
    formant_ceiling_hz = 5000
    window_length_s = 0.025
    pre_emphasis = 50
    formants = praat.call(
        sound,
        "To Formant (burg)",
        timestep_s,
        max_formants,
        formant_ceiling_hz,
        window_length_s,
        pre_emphasis,
    )

    dataDict = {}
    # extract the formants from the vowels in the 0th tier
    for vowels in soundTextgrid[0]:
        if vowels.mark == "":
            continue
        time = (vowels.minTime + vowels.maxTime) / 2.0
        f1 = praat.call(formants, "Get value at time", 1, time, "Hertz", "Linear")
        f2 = praat.call(formants, "Get value at time", 2, time, "Hertz", "Linear")
        f3 = praat.call(formants, "Get value at time", 3, time, "Hertz", "Linear")
        f1 = round(f1, 2)
        f2 = round(f2, 2)
        f3 = round(f3, 2)

        data.append(
            {
                "timestamp": round(time, 4),
                "vowel": vowels.mark,
                "F1": f1,
                "F2": f2,
                "F3": f3,
            }
        )
    # pprint.pprint(data)
    # print(len(data))
    return data


if __name__ == "__main__":
    main()
