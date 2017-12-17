#this file converts the .wav file to text.
#we first extract the wav format from Audacity
#Google speech reconition Api is used


import speech_recognition as sr

def conText(fileName):
    r = sr.Recognizer()
    with sr.AudioFile(fileName) as source:
        print("Input from the wav file :" + fileName)
        print("Processing the audio...")
        # r listen works for the wav files , not limited only ti the input from the microphone
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        textFromAudio = r.recognize_google(audio)

        return textFromAudio
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Questions
# 1. Why the wav file is limited to the size?
#large files do not work

def main():
    # fileName = input("Enter the file in wav format")
    fileName = '/Users/chandinisingh/Desktop/IndependentStuy/SampleVideoFile/audio2.wav'
    textFromAudio = conText(fileName)

    f = open("TextFromWav2","w")

    f.write(textFromAudio)
    print(textFromAudio)
if __name__ == "__main__":
   main()