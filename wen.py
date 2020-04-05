import tkinter as tk
from tkinter import *
import webbrowser

win=tk.Tk()
win.title("WebBrowser")
win.geometry("250x150")


def google():
    webbrowser.open("www.google.com")

def youtube():
    webbrowser.open("www.youtube.com")

def facebook():
    webbrowser.open("www.facebook.com")

def geeksforgeeks():
    webbrowser.open("www.geeksforgeeks.com")

google=tk.Button(win,text="igoogle", command=google)
google.grid(row=0,column=0)

youtube=tk.Button(win,text="iyoutube", command=youtube)
youtube.grid(row=0,column=1)

facebook=tk.Button(win,text="ifacebook", command=facebook)
facebook.grid(row=1,column=0)

geeksforgeeks=tk.Button(win,text="igeeksforgeeks", command=geeksforgeeks)
geeksforgeeks.grid(row=1,column=1)



exit_button=tk.Button(win, text="exit", command=win.quit)
exit_button.grid(row=2,column=1)
win.mainloop()

