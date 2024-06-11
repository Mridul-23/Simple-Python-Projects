import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pyttsx3
import keyboard

# Initializing our TTS Engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')


def mspeak() -> None:
    engine.setProperty('voice', engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'))
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

def femspeak() -> None:
    engine.setProperty('voice', engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'))
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

def quit_application() -> None:
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        root.quit()


# Initializing our GUI
root = Tk()

root.title("Text To Speech")
root.geometry("780x450")
root.configure(bg='#2c2f34')

ic = PhotoImage(file='robot.png')
root.iconphoto(False, ic)

textv = StringVar()
fontst = ("Arial Bold", 30)
fonts = ("Open sans", 20)
fontb = ("Helvetica", 18)

# Adding main Frame
obj = LabelFrame(root, text="Welcome to Text to Speech", font=fontst, bd=2, labelanchor='n', bg = '#25292e', fg='#00FFFF', relief='solid')
obj.pack(fill='both', expand='yes', padx=10, pady=10)

# Adding Label
lbl = Label(obj, text='Enter the text below', font=fonts, bd=5, justify='center', bg='#25292e', fg='#FFFFFF')
lbl.pack(side=tk.TOP, padx=5, pady=20)

# Adding input section
text = Entry(obj, textvariable=textv,font=fonts, width=40, bd=0)
text.pack(side=tk.TOP, padx=10, pady=10)

# Adding a button
btn = Button(obj, text='Speak in male voice', font=fontb, bg='black', fg='white', command=mspeak, borderwidth=0.5, relief='solid')
btn.pack(side=tk.LEFT, padx=35)

#Adding another button
btn2 = Button(obj, text='Speak in female voice', font=fontb, bg='black', fg='white', command=femspeak, borderwidth=0.5, relief='solid')
btn2.pack(side=tk.RIGHT, padx=35)

qt = Button(obj, text='QUIT NOW', command=quit_application, bg="red", fg="white", font=("Helvetica", 15, "bold"), width=10, borderwidth=0.1, relief='solid')
qt.pack(side=tk.BOTTOM, pady=23)

# Adding Keyboard Functionings
keyboard.add_hotkey('enter', mspeak)

root.mainloop()