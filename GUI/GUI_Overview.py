"""
Python provides various options for developing graphical user interfaces (GUIs).

Tkinter: Tkinter is the Python interface to the Tk GUI toolkit shipped with Python.

wxPython: This is an open-source Python interface for wxWidgets GUI toolkit.

PyQt:This is also a Python interface for a popular cross-platform Qt GUI library.
"""

# 1. import Tkinter  # Import the Module

# 2. Create the GUI application Main Window

# 3. Add one or more of the below-mentioned widgets to the GUI application.

# 4. Enter the main event loop to take action against each event triggered by the user.

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("500x500")

"""
1. pack() : Organizes widgets in Blocks before placing them in the parent widget
2. grid() Method - This geometry manager organizes widgets in a table-like
structure in the parent widget.
3. place() Method -This geometry manager organizes widgets by placing them in a
specific position in the parent widget.
"""

def helloCallBack():
    msg = messagebox.showinfo("Home","Welcome to Python World")

B = Button(top, text="Click to Login", command = helloCallBack)

B.place(x=10,y=10)

top.mainloop()