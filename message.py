from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()

root.title("Messages")


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno these are the different types boxes we can create

def mypopup():
     messagebox.showinfo("This is information", "you are Breathtaking")  # first argument is the name of the message
    # box and second argument is the message inside the message box
     messagebox.showwarning("This is title","This is a warning")
     messagebox.showerror("This is title", "This is an error")
     messagebox.askquestion("This is title", "This is a question")
     messagebox.askokcancel("This is title", "asking ok or cancel")
     response=messagebox.askyesno("This is title", "just asking")
     #mylabel=Label(root, text=response).pack()
     if response==1:
         mylabel=Label(root, text="SHE SAID YES").pack()
     else:
         mylabel=Label(root, text="OOPS DIL TOOT GYA").pack()






my_button = Button(root, text="popup", command=mypopup).pack()

root.mainloop()
