#NOTE: the file name cannot be tkinter.py!!
import tkinter as tk
from tkinter import ttk

#tk._test()

root = tk.Tk()

ttk.Label(root, text="Steganography`", padding=(30,10)).pack()  #center aligned and packed
#ttk.Label(root, text="Hello World!").grid() ----not center aligned

root.mainloop()