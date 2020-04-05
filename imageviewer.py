from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Image viewer app")
root.iconbitmap('facebook.png')


# creating image objects for respective images
my_img1 = ImageTk.PhotoImage(Image.open("facebook.png"))
my_img2 = ImageTk.PhotoImage(Image.open("youtube.png"))
my_img3 = ImageTk.PhotoImage(Image.open("ironman.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("groot.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("HackerRank_logo1.png"))
# made a list of all the images
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]
# made label to display the image
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

status = Label(root, text="Image 1 of " + str(len(image_list)))


# defining button functions
def forward_button(image_number):
    global my_label
    global my_button1
    global my_button2
    my_label.grid_forget()  # to delete the previous image so that the new img dont overalap
    my_label = Label(image=image_list[image_number - 1])  # same label for this button to display the image
    my_button2 = Button(root, text=">>", command=lambda: forward_button(image_number + 1)).grid(row=1,column=2)  # need to desplay both the buttons
    my_button1 = Button(root, text="<<", command=lambda: forward_button(image_number - 1)).grid(row=1, column=0)
    if image_number == 5:
        my_button2 = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)))
    status.grid(row=2, column=0, columnspan=3)


def back_button(image_number):
    global my_label
    global my_button1
    global my_button2

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    my_button2 = Button(root, text=">>", command=lambda: forward_button(image_number + 1)).grid(row=1, column=2)
    my_button1 = Button(root, text="<<", command=lambda: forward_button(image_number - 1)).grid(row=1, column=0)

    if image_number == 1:
        my_button1 = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)))
    status.grid(row=2, column=0, columnspan=3)


my_button2 = Button(root, text=">>", command=lambda: forward_button(2)).grid(row=1, column=2)
my_button1 = Button(root, text="<<", command=back_button, state=DISABLED).grid(row=1, column=0)
my_button3 = Button(root, text="EXIT", command=root.quit).grid(row=1, column=1)

status.grid(row=2, column=0, columnspan=3)

root.mainloop()
