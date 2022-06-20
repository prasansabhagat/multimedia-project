#NOTE: the file name cannot be tkinter.py!!
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import os
#from turtle import width

def TextInImage(frame):
    frame.destroy()
    frame = LabelFrame(root, text="Image Steganography", padx=20, pady=20)
    frame.pack(padx=30, pady=20)
    text_in_image = Label(frame, text="Text in Image")
    text_in_image.grid(row=0)

    encode_text_button = Button(frame, text="Encode", command=lambda:encode_text(frame))
    encode_text_button.grid(row=1, column=0, pady=20)

    decode_text_button = Button(frame, text="Decode", command=lambda: decode_text(frame))
    decode_text_button.grid(row=2, column=0, pady=20)

    home_button = Button(frame, text="Home", command= lambda: home(frame) )
    home_button.grid(row = 3, column = 0, pady=20)
    #print("Encode!!")

def home(frame):
    frame.destroy()
    frame = LabelFrame(root, text="Image Steganography", padx=30)
    frame.pack(padx="30", pady=50)

    option1_button = ttk.Button(frame, text="Text in Image", command=lambda:TextInImage(frame))
    option1_button.pack( fill="x",padx="30", pady="10")

    option2_button = ttk.Button(frame, text="Image in Image", command=lambda:ImageInImage(frame))
    option2_button.pack( fill="x",padx="30", pady="10")

    quit_button = ttk.Button(frame, text="Quit", command=root.destroy)
    quit_button.pack(pady="10")


def encode_text(frame):
    frame.destroy()
    frame = LabelFrame(root, text="Text in Image", padx=20, pady = 10)
    frame.pack()
    select_image = Label(frame, text="Select the Image in which you want to hide text:")
    select_image.grid(row=0)

    select_button = Button(frame, text = "Select", command=lambda:open_file(frame))
    select_button.grid(row=1, column=0, pady=10)

    type_text = Label(frame, text="Enter the message you want to hide:")
    type_text.grid(row=2, column = 0)

    textbox = Text(frame, height= 3, width = 10)
    textbox.grid(row=3, column=0)

    print(my_img)

    hide_button = Button(frame, text="Hide",command=lambda: encode_function(textbox ))
    hide_button.grid(row=4, column = 0)

    home_button = Button(frame, text="Home", command=lambda: home(frame))
    home_button.grid(row=5, column=0, pady=20)

#function to enter hidden text
def encode_function(textbox, my_img):
    print("ji")

#function to open file
def open_file(frame):
    e_pg = Frame(root)
    my_file = fd.askopenfilename(filetypes=([('png', '.png'), ('jpeg', '.jpeg'), ('jpg', '.jpg'), ('All Files', '.*')]))
    if not my_file:
        tk.messagebox.showerror("Error", "You have selected nothing !")
    else:
        my_img = Image.open(my_file)
        new_image = my_img.resize((300, 200))
        img = ImageTk.PhotoImage(new_image)
        label3 = Label(frame, text='Selected Image')
        label3.config(font=('Helvetica', 14, 'bold'))
        label3.grid(row=5, column = 0)
        board = Label(frame, image=img)
        board.image = img
        board.grid(row=6, column = 0)
        print("image loaded")

def decode_text(frame):
    frame.destroy()
    frame = LabelFrame(root, text="Text in Image", padx=20, pady=10)
    frame.pack()

    select_encoded_image = Label(frame, text="Select the image with hidden text:")
    select_encoded_image.grid(row = 1, column = 0, pady = 10)

    select_button = Button(frame, text="Select", command = lambda:open_file(frame))
    select_button.grid(row=2, column=0, pady=10)

    home_button = Button(frame, text="Home", command=lambda: home(frame))
    home_button.grid(row=3, column=0, pady=20)

def ImageInImage(frame):
    frame.destroy()
    frame = LabelFrame(root, text="Image Steganography", padx=20, pady=20)
    frame.pack(padx=30, pady=20)
    text_in_image = Label(frame, text="Image in Image")
    text_in_image.grid(row=0)

    encode_image_button = Button(
        frame, text="Encode", command=lambda: encode_image(frame))
    encode_image_button.grid(row=1, column=0, pady=20)

    decode_image_button = Button(
        frame, text="Decode", command=lambda: decode_image(frame))
    decode_image_button.grid(row=2, column=0, pady=20)

    home_button = Button(frame, text="Home", command=lambda: home(frame))
    home_button.grid(row=3, column=0, pady=20)

    print("Encode!!")

#root properties
root = tk.Tk()
root.geometry("400x400")
root.title("Steganography")

#frame properties
frame = LabelFrame(root, text="Image Steganography", padx=30)
frame.pack(padx="30", pady=50)

option1_button = ttk.Button(frame, text="Text in Image", command=lambda:TextInImage(frame))
option1_button.pack( fill="x",padx="30", pady="10")

option2_button = ttk.Button(frame, text="Image in Image", command=lambda:ImageInImage(frame))
option2_button.pack( fill="x",padx="30", pady="10")

quit_button = ttk.Button(frame, text="Quit", command=root.destroy)
quit_button.pack(pady="10")

root.mainloop()