from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("400x250")
root.title("File Converter")

frame = Frame(root)
frame.pack()

text = Text(frame, height= 20, width= 70)

def openFileDialog():
    file_path = filedialog.askopenfilename()
    text.insert("1.0", file_path)

button = Button(frame, text = "Select File", command=openFileDialog)
button.pack(pady= 50)
text.pack(expand= True)

root.mainloop()