from tkinter.filedialog import askopenfilename
import os

dwc = os.getcwd()
username = os.getlogin()

def Selector():
    path =  askopenfilename(initialdir= fr"{dwc}\Themes", title="Select Theme")
    ext = os.path.splitext(path)
    if ext[1] == '.theme':
        return path
    else:
        path = Selector()
        return path