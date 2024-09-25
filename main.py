from tkinter import *
import Steal as S
import Loot as L

#Window
window = Tk()
window.title("SaLoPH PROTOTYPE")
window_width = 270
window_height = 100
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_x = int((screen_width / 2) - (window_width / 2))
position_y = int(((screen_height / 2)) - (3 * (window_height / 2)))
window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

window.resizable(False, False)

#Executable functions
button = Button(window, text="Export")
button2 = Button(window, text="Import")

#Import Button
button.config(command=S.Steal)
button.config(font=('monocraft', 20, 'bold'))
button.place(x=450, y=200)
button.pack(side=RIGHT, padx=1, pady=1)

#Export button
button2.config(command=L.Apply)
button2.config(font=('monocraft', 20, 'bold'))
button2.place(x=450, y=200)
button2.pack(side=LEFT, padx=1, pady=1)

window.mainloop()