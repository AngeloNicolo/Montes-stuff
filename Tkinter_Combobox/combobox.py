# brings classes and function 
import tkinter as tk 
from tkinter import ttk


#Defining the event when selected.
def on_select(event):

    selected_item = event.widget.get()
    print("Selected item:", selected_item)

#Window title comes back with text.
root = tk.Tk()
root.title("Combobox Example")

# List of items in a Array.
items = ["item 1", "item2", "item3", "item4", "item5"]

# Connect the Array to the combobox.
combo_box = ttk.Combobox(root, values=items)
combo_box.bind("<<ComboboxSelected>>", on_select)

combo_box.pack()

root.mainloop()