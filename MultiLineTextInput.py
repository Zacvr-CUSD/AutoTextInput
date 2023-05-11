#Import tkinter for the GUI and PyAutoGUI to input text
from tkinter import *
import pyautogui

# create window
window = Tk()
window.title("AutoTextInput")
window.geometry("365x265")
window.resizable(False,False)
window.attributes('-topmost',True)
# create textbox
text_box = Text(window, height=12, width=38,font='helvetica')
text_box.place(x=1,y=1)

# create scrollbar
scrollbar = Scrollbar(window, command=text_box.yview)
scrollbar.place(x=348,y=1,height=220)
text_box.config(yscrollcommand=scrollbar.set)

# create button to automatically input text
def button_clicked():
    for i in range(5, 0, -1):
        window.title('Inputting Text In ' +str(i))
        button.config(text='Inputting Text In ' +str(i))
        window.update()
        window.after(1000)
        window.title("AutoTextTyper")
        button.config(text="Send Text")
        window.update()
    pyautogui.typewrite(text_box.get("1.0", "end-1c"))

# create button to input text slowly ('interval' changes speed)
def button_clickedDelayed():
    for i in range(5, 0, -1):
        window.title('Inputting Text In ' +str(i))
        button2.config(text='Inputting Text In ' +str(i))
        window.update()
        window.after(1000)
        window.title("AutoTextTyper")
        button2.config(text="Send Delayed Text")
        window.update()
    pyautogui.typewrite(text_box.get("1.0", "end-1c"), interval=.02)

#clear the text_box text
def button_clear_text():
    text_box.delete(1.0,"end")


# button to input text all at once after 4-5 seconds
button = Button(window, text="Send Quick Text", command=button_clicked)
button.place(x=5,y=230)

# button to input text in a quick typing fashion after 4-5 seconds
button2 = Button(window, text="Send Delayed Text", command=button_clickedDelayed)
button2.place(x=131,y=230)

# button to clear all text in the input text box
button3 = Button(window, text="Clear All Text", command=button_clear_text)
button3.place(x=267,y=230)

# run window
window.mainloop()
