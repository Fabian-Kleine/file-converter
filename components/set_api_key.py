from tkinter import *
from tkinter.ttk import *
import webbrowser
from .open_window.open_select_window import OpenSelectWindow

def SetAPIKeyWindow():
    root = Tk()
    root.geometry("600x450")
    root.title("Set Convert API Secret")

    frame = Frame(root)
    frame.pack()

    text = Label(frame, text= "You can get your API Secret on convertapi.com")
    text.pack()

    def open_website():
        webbrowser.open("https://www.convertapi.com/a/signin", new=0, autoraise=True)

    open_website_button = Button(frame, text="Get API Secret", command= open_website)
    open_website_button.pack(pady= 10)

    api_secret_label = Label(frame, text="Your API Secret")
    api_secret_input = Entry(frame)

    api_secret_label.pack()
    api_secret_input.pack()

    def apply_api_secret():
        api_secret = api_secret_input.get()
        env_file = open(".env", "w")
        env_file.write("API_SECRET = " + api_secret)
        env_file.close()
        root.destroy()
        OpenSelectWindow()

    apply_button = Button(frame, text= "Apply API Secret", command= apply_api_secret)
    apply_button.pack(pady= 5)

    root.mainloop()