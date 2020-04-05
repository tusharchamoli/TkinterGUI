import tkinter as tk
from gtts import gTTS
from playsound import playsound
win = tk.Tk()
win.title("Text to speech")
win.geometry("200x200")

def text_to_speech() :
     text = entry.get()
     speech = gTTS(text=text,lang="en")
     speech.save(r'I:\youtube\speech.mp3') # save the file to your desired location
     playsound(r'I:\youtube\speech.mp3')
     
     
label = tk.Label(win,text="Enter text here")
label.grid(row=0,column=0)

entry = tk.Entry(win)
entry.grid(row=1,column=0)

button=tk.Button(win,text="GO",command=text_to_speech)
button.grid(row=1,column=1)

win.mainloop()


