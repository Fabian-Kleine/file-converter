from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

root = Tk()
root.geometry("600x450")
root.title("File Converter")

frame = Frame(root)
frame.pack()

text = Label(frame, font=(25))

def openFileDialog():
    file_path = filedialog.askopenfilename()
    if (file_path): 
        text.config(text="File Path: "+file_path)
        continueButton.config(state= NORMAL)

selectFileButton = Button(frame, text = "Select File", command=openFileDialog)
selectFileButton.pack()
text.pack(expand= True)

continueButton = Button(frame, text="Convert", state= DISABLED)
continueButton.pack(pady=20)

root.mainloop()