from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from .open_window.open_converter_window import OpenConverterWindow

def SelectWindow():
    root = Tk()
    root.geometry("600x450")
    root.title("File Converter")

    frame = Frame(root)
    frame.pack()

    frame2 = Frame(root)
    frame2.pack()

    text = Text(frame2, font=(25), state= DISABLED)
    file_path_label = Label(frame2, font=(25), foreground= "#000", text="File Path:", anchor="e")

    def openFileDialog():
        global file_path
        file_path = filedialog.askopenfilename()
        if (file_path):
            text.config(state= NORMAL)
            text.delete("1.0", "end")
            text.insert("1.0", file_path)
            text.config(state= DISABLED)
            continueButton.config(state= NORMAL)

    selectFileButton = Button(frame, text = "Select File", command=openFileDialog)
    selectFileButton.grid(row=0, column=0, padx='5', pady='5')

    def openConverterWindow():
        root.destroy()
        OpenConverterWindow(file_path)


    continueButton = Button(frame, text="Convert", state= DISABLED, command=openConverterWindow)
    continueButton.grid(row=0, column=2, padx='5', pady='5')

    file_path_label.pack()
    text.pack(padx='5', pady='5')

    root.mainloop()