#NOTE: the file name cannot be tkinter.py!!
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import os

#function for text in image 
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

#home function
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

#function to encode text
def encode_text(frame):
    frame.destroy()
    frame = LabelFrame(root, text="Text in Image", padx=20, pady = 10)
    frame.pack()
    select_image = Label(frame, text="Select the Image in which you want to hide text:")
    select_image.grid(row=0)

    select_button = Button(frame, text = "Select", command=lambda:open_encode_file(frame))
    select_button.grid(row=1, column=0, pady=10)

    type_text = Label(frame, text="Enter the message you want to hide:")
    type_text.grid(row=2, column = 0)

    textbox = Text(frame, height= 3, width = 10)
    textbox.grid(row=3, column=0)

    hide_button = Button(frame, text="Hide",command=lambda: encode_function(textbox ,my_img))
    hide_button.grid(row=4, column = 0)

    home_button = Button(frame, text="Home", command=lambda: home(frame))
    home_button.grid(row=5, column=0, pady=20)

#function to generate text data(message to hide) to binary
def generate_data(data):
    new_data = []
    for i in data:
        new_data.append(format(ord(i), "08b"))  
        #format(14, '08b') --> 00001110 , coverts to 8bit binary
        #ord function returns the ascii(unicode value) value
    print("new data")
    print(new_data)
    return new_data

#function to modify the pixels of image
def modify_pixel(pixel, data):
    data_list = generate_data(data)
    data_length = len(data_list)
    print(data_length)
    image_data = iter(pixel) 
    print(image_data)
    print("bye")
    #iter --> function creates an object which can be iterated one element at a time.
    for i in range(data_length):
        pixel = [value for value in image_data.__next__()[:3] + image_data.__next__()[:3] + image_data.__next__()[:3]]
        for j in range(0, 8):
            if (data_list[i][j] == '0') and (pixel[j] % 2 != 0):
                if (pixel[j] % 2 != 0):
                    pixel[j] -= 1

                elif (data_list[i][j] == '1') and (pixel[j] % 2 == 0):
                    pixel[j] -= 1

        if (i == data_length - 1):
            if (pixel[-1] % 2 == 0):
                pixel[-1] -= 1
        else:
            if (pixel[-1] % 2 != 0):
                pixel[-1] -= 1

        pixel = tuple(pixel)
        yield pixel[0:3]
        yield pixel[3:6]
        yield pixel[6:9]



#function to enter the data pixels in image
def encode_data_pixels(new_img, data):
    w = new_img.size[0]
    (x,y) = (0,0)
    for pixels in modify_pixel(new_img.getdata(), data):
        print("bye")

#function to enter hidden text
def encode_function(textbox, my_img):
    global data
    data = textbox.get("1.0", "end-1c")
    if (len(data) == 0):
        tk.messagebox.showinfo("Alert", "Kindly enter text in TextBox")
    else:
        global new_img
        new_img = my_img.copy()
        encode_data_pixels(new_img, data)


#function to open file for encoding
def open_encode_file(frame):
    e_pg = Frame(root)
    my_file = fd.askopenfilename(filetypes=([('png', '.png'), ('jpeg', '.jpeg'), ('jpg', '.jpg'), ('All Files', '.*')]))
    if not my_file:
        tk.messagebox.showerror("Error", "You have selected nothing !")
    else:
        global my_img
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

#function to open decode file
def open_decode_file(frame):
    d_F3 = Frame(root)
    my_file = fd.askopenfilename(filetypes=(
        [('png', '.png'), ('jpeg', '.jpeg'), ('jpg', '.jpg'), ('All Files', '.*')]))
    if not my_file:
        tk.messagebox.showerror("Error", "You have selected nothing !")
    else:
        global my_img_decode
        my_img_decode = Image.open(my_file, 'r')
        my_image = my_img_decode.resize((300, 200))
        img = ImageTk.PhotoImage(my_image)
        label4 = Label(frame, text='Selected Image :')
        label4.config(font=('Helvetica', 14, 'bold'))
        label4.grid(row=5, column=0)
        board = Label(frame, image=img)
        board.image = img
        board.grid(row=6, column=0)

#function for decode text
def decode_text(frame):
    frame.destroy()
    frame = LabelFrame(root, text="Text in Image", padx=20, pady=10)
    frame.pack()

    select_encoded_image = Label(frame, text="Select the image with hidden text:")
    select_encoded_image.grid(row = 1, column = 0, pady = 10)

    select_button = Button(frame, text="Select", command = lambda:open_decode_file(frame))
    select_button.grid(row=2, column=0, pady=10)

    home_button = Button(frame, text="Home", command=lambda: home(frame))
    home_button.grid(row=3, column=0, pady=20)

#function for image in image
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