from tkinter import *
from tkinter.ttk import *

def ConverterWindow(file_path):
    root = Tk()
    root.geometry("600x450")
    root.title("File Converter")

    frame = Frame(root)
    frame.pack()

    text = Label(frame, font=(25), state= DISABLED, text=file_path)
    text.pack()

    root.mainloop()