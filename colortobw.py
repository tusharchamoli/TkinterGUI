from PIL import ImageTk, Image
open_image=Image.open(r'facebook.png')
b_w_image=open_image.convert("L")
b_w_image.show()