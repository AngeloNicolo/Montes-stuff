# brings classes and function 
import tkinter as tk 
from tkinter import ttk


#Defining the event when selected.
def on_select(event):

    selected_item = event.widget.get()
   print("Selected item;", selected_item)

#Window title comes back with text.
root = tk.Tk()
root.tile("Combobox Example")
