# Text to Speech Converter

Take a text file and output the content as an mp3 file

## Set up
### Requirements
* Python: You can check if it's already on your machine by opening terminal and running `python --version`. Install python with [this guide](https://docs.python-guide.org/starting/installation/)
* Pip: You can check if it's already on your machine by opening terminal and running `pip`. Install pip with [this guide](https://pip.pypa.io/en/stable/installing/)
* [gTTS](https://pypi.org/project/gTTS/): Install using `pip install gTTS`

## Usage
In terminal navigate to the directory the `convertTextToSpeech.py` script is in. Create a text file with the text you want to convert to speech. Run:
```
python convertTextToSpeech.py filename.txt
```
This will create an audio file (`.mp3`) with the same name as the text file