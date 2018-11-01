from gtts import gTTS
import sys

try:
    filename = sys.argv[1]
except IndexError:
    print "No text file provided. Please provide a *.txt file."
    sys.exit(1)

f = open(filename, "r")
content = f.read()
tts = gTTS(content)
mp3Filename = filename.replace('txt', 'mp3')
tts.save(mp3Filename)