#tkinter module, brings classes and function for making graphical user interfaces.
import tkinter as tk

#When button is clicked, it will print "Button clicked!"
def button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("Button Example")

#Function will be called when the button is clicked, while also adding buttons to the window to desplay  them.
button = tk.Button(root,text="Click Me!", command=button_click)
button.pack()

#keeps window open til user closes it, also listens and responds to the user.
root.mainloop()