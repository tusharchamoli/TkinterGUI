import speech_recognition as sr
r=sr.Recognizer()
a=sr.AudioFile('Recording.wav') # record your voice and save it to the directory
with a as source:
    audio=r.record(source)

text=r.recognize_google(audio)

file1=open(r"C:\Users\Tushar\PycharmProjects\gui\1.txt","a")
file1.writelines(text)
file1.close()