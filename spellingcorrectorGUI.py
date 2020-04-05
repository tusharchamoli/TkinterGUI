from textblob import TextBlob
from tkinter import *
root = Tk()

root.title("Spell Corrector app")
root.geometry("400x400")


def spellcorrect():
    a = entry.get()
    b = TextBlob(a)
    my_label2 = Label(root, text=b.correct())
    my_label2.grid(row=2, column=0)
    entry.delete(0, END)


my_label = Label(root, text="Enter your sentence")
my_label.grid(row=0, column=0)

entry = Entry(root, width=30)
entry.grid(row=0, column=1)

my_button = Button(root, text="SUBMIT", command=spellcorrect)
my_button.grid(row=1, column=1)

root.mainloop()
