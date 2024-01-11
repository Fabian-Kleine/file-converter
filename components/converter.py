from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfile
from dotenv import load_dotenv
import os
from pathlib import Path
import convertapi
from .open_window.open_select_window import OpenSelectWindow

def ConverterWindow(file_path):
    load_dotenv()

    api_secret = os.getenv("API_SECRET")

    convertapi.api_secret = api_secret

    def openSelectWindow():
        root.destroy()
        OpenSelectWindow()


    def convert():
        convert_button.config(text= 'Loading...', state= DISABLED)
        try: 
            file_type = clicked_dropdown.get()
            file_name = Path(file_path).stem + '.' + file_type
            result = convertapi.convert(file_type, {'File': file_path})
            new_file_path = asksaveasfile(mode= 'a', initialfile= file_name)
            result.file.save(new_file_path.name)
        except:
            errorMsg.config(text = 'An error occured!')
            convert_button.config(text= 'Convert', state= NORMAL)
        convert_button.config(text= 'Convert another file', state= NORMAL, command= openSelectWindow)

    root = Tk()
    root.geometry("600x450")
    root.title("File Converter")

    frame = Frame(root)
    frame.pack()

    file_options = [
        "pdf",
        "pdf",
        "png",
        "jpg",
        "webp",
        "html",
        "csv",
        "docx",
        "xlsx"
    ]

    clicked_dropdown = StringVar()
    clicked_dropdown.set("pdf")

    dropdown_label = Label(frame, text= "Select New File Format:")
    dropdown_label.pack()

    dropdown = OptionMenu(frame, clicked_dropdown, *file_options)
    dropdown.pack()

    errorMsg = Label(frame, foreground= 'red')
    errorMsg.pack()

    convert_button = Button(frame, text= 'Convert', command= convert)
    convert_button.pack()

    root.mainloop()