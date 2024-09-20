import os
import ctypes
from win32com.shell import shell, shellcon
dwc = os.getcwd()


def Apply(theme_name):
    theme =  fr"{dwc}\Themes\{theme_name}.theme"
    shell.SHChangeNotify(shellcon.SHCNE_ASSOCCHANGED, shellcon.SHCNF_IDLIST, None, None)
    os.system(f'rundll32.exe shell32.dll,Control_RunDLL desk.cpl,,@themes /Action:OpenTheme /File:"{theme}"')
