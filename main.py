from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from components import select, set_api_key
import os

api_secret = os.getenv("API_SECRET")

if api_secret:
    select.SelectWindow()
else:
    messagebox.showerror('API Secret Error', 'No API Secret Set!')
    set_api_key.SetAPIKeyWindow()

