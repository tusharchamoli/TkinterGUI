from tkinter import *
from better_profanity import profanity
from PIL import ImageTk, Image

root = Tk()

root.title("Image viewer app")
root.iconbitmap('download.ico')
root.geometry("400x400")

def filterwords():
    word = entry.get()
    if __name__ == '__main__':
        profanity.load_censor_words()
        x = word
        output = profanity.censor(x)
    my_label2 = Label(root, text=output)
    my_label2.grid(row=2, column=0)
    entry.delete(0,END)


my_label = Label(root, text="Enter your sentence")
my_label.grid(row=0, column=0)

entry = Entry(root, width=30)
entry.grid(row=0, column=1)

my_button = Button(root, text="SUBMIT", command=filterwords)
my_button.grid(row=1, column=1)

root.mainloop()
