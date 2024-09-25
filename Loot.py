import os
import shutil
from Selector import Selector

def Apply():
    themePath = Selector()
    username = os.getlogin()
    dst = fr"C:\Users\{username}\AppData\Local\Microsoft\Windows\Themes"
    shutil.copy(themePath, dst)
    if os.path.exists(themePath):
        os.system(f'start {themePath}')
    else:
        print("This is not a valid .theme file.")