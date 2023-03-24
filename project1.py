from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from pygame import mixer
import threading
import datetime
import time

root = Tk()
root.geometry("500x300")
label= Label(root, text="Alarm Clock", bg="grey", font="comicsans 20 bold", relief=SUNKEN)
label.grid(row=0, column=0, columnspan=5)

alarmtime= StringVar()
showmsg= StringVar()
def alarm():
    a= alarmtime.get()

    AlarmTime= a
    Currentime= time.strftime("%H:%M")

    while AlarmTime != Currentime:
        Currentime= time.strftime("%H:%M")

    if AlarmTime == Currentime:
        mixer.init()
        mixer.music.load("C:\\sound\\file_example_MP3_700KB.mp3")
        mixer.music.play()
        msg = messagebox.showinfo('Info', f"{showmsg.get()}")
        if msg == 'ok':
            mixer.music.stop()


image= Image.open("C:\\Users\\HP\\Pictures\\img.png")
ph= image.resize((150,180))
photo= ImageTk.PhotoImage(ph)
Label(image= photo).grid(row=3,column=0, rowspan=4, padx=10, pady=10)

timein= Label(root, text="Input Time", font="comicsans 13 bold")
timein.grid(row=3, column=2)
inptime= Entry(root, font="comicsans 10", width=10, textvariable=alarmtime)
inptime.grid(row=3, column=4)

msg= Label(root, text="Message", font="comicsans 13 bold")
msg.grid(row=4,column=2, columnspan=3)
inpmsg= Entry(root, font="comicsans 10", textvariable=showmsg)
inpmsg.grid(row=5, column=2, columnspan=3)

submit= Button(root, text="SUBMIT",font="comicsans 10 bold", command=alarm)
submit.grid(row=6, column=2, columnspan=3)

root.mainloop()

