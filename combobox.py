#
import tkinter as tk 
from tkinter import ttk


#
def on_select(event):

    selected_item = event.widget.get()
   print("Selected item;", selected_item)

#
rooot = tk.Tk()
root.tile("Combobox Example")
