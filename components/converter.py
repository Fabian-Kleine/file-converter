from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfile
from dotenv import load_dotenv
import os
from pathlib import Path
import convertapi
from convertapi.exceptions import ApiError
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
        errorMsg.config(text = '')
        try: 
            file_type = clicked_dropdown.get()
            file_name = Path(file_path).stem + '.' + file_type
            result = convertapi.convert(file_type, {'File': file_path})
            new_file_path = asksaveasfile(mode= 'a', initialfile= file_name)
            result.file.save(new_file_path.name)
            errorMsg.config(text = 'Success!', foreground= 'green')
        except ApiError as api_error:
            error_message = str(api_error)
            start_index = error_message.find("Unsupported conversion")  # Find the starting index of the relevant information
            end_index = error_message.find("']", start_index) + 1

            unsupported_conversion_info = error_message[start_index:end_index]

            errorMsg.config(text=f'Conversion error: {unsupported_conversion_info}')
            print(unsupported_conversion_info)
        except Exception as error:
            errorMsg.config(text='An error occurred!')
            print(error)
        finally:
            convert_button.config(text='Convert', state=NORMAL)
            

    root = Tk()
    root.geometry("600x450")
    root.title("File Converter")

    frame = Frame(root)
    frame.pack()

    frame2 = Frame(root)
    frame2.pack()

    frame3 = Frame(root)
    frame3.pack()

    file_options = [
        "pdf",
        "pdf",
        "png",
        "jpg",
        "webp",
        "svg",
        "html",
        "md",
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

    return_button = Button(frame2, text= 'Convert another file', command= openSelectWindow)
    return_button.grid(row=0, column=0, padx='5', pady='5')

    convert_button = Button(frame2, text= 'Convert', command= convert)
    convert_button.grid(row=0, column=2, padx='5', pady='5')

    file_path_text = Text(frame3, font=(25))
    file_path_text.insert("1.0", file_path)
    file_path_text.config(state= DISABLED)
    file_path_text.pack(padx='5', pady='5')

    root.mainloop()