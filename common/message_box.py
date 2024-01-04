#import ctypes
import easygui

import sys
import tkinter.messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename

########### insructions ###########
#
#   brew install python-tk@3.9
#
###################################






# def hello():
#     messagebox.showinfo("Say Hello", "Hello World")

if __name__ == "__main__":
    root = Tk()
    is_ip_config_correctly = tkinter.messagebox.askyesno("Manual validation", "is ip address configured correctly")
    # Button(root, text='File Open', command=openFile).pack(fill=X)
    # mainloop()

    # root = tk.Tk()
    # tk.messagebox.askyesno("Manual validation", "is ip address configured")
    #
    # w = tk.Label(root, text="Hello, world!")
    # w.pack()
    print("===============")
    print("+++++++++++++++")
