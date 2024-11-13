import parselmouth
from parselmouth import praat
import textgrid

tg = textgrid.TextGrid.fromFile("MisingSentences/An1/voice9.TextGrid")
sound = parselmouth.Sound("MisingSentences/V1/voice9.wav")

formants = praat.call(sound, "To Formant (burg)", 0.0025, 5, 5000, 0.025, 50)

f1List = []
f2List = []
f3List = []

print("------- IntervalTier Example -------")
print(tg)
print(tg[0])

print(tg[0][1].minTime)
print(tg[0][1].maxTime)
print(tg[0][1].mark)

t1Min = tg[0][1].minTime
t1Max = tg[0][1].maxTime
t1 = (t1Min + t1Max) / 2.0
f1 = praat.call(formants, "Get value at time", 1, t1, "Hertz", "Linear")
f2 = praat.call(formants, "Get value at time", 2, t1, "Hertz", "Linear")
f3 = praat.call(formants, "Get value at time", 3, t1, "Hertz", "Linear")

print(f1)
print(f2)
print(f3)
