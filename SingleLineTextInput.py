#rough first draft of the multi line auto text input

import os
import tkinter as tk
import time
import pyautogui

basedir = os.path.dirname(__file__)

root = tk.Tk()
root.title("Auto Text Input")
root.iconbitmap(os.path.join(basedir, "Logo.ico"))
root.resizable(False,False)
root.attributes('-topmost',True)
canvas1 = tk.Canvas(root, width=250, height=50)
canvas1.pack()


inputtext = tk.Entry(root)
canvas1.create_window(125, 15, window=inputtext,width=235)
#set window color

def Type_Text():
    count = 4
    while count >= 1:
        count_string = str(count)
        label1 = tk.Label(root, text='Typing text in '+count_string, fg='blue', font=('helvetica', 11, 'bold'))
        canvas1.create_window(155, 40, window=label1)
        canvas1.update_idletasks()
        #canvas1.update()
        time.sleep(1)
        count -= 1
        label1.destroy()
        if count == 0:
            InputText = inputtext.get()
            pyautogui.write(InputText)
            label2 = tk.Label(root, text='Text has been input', fg='green', font=('helvetica', 12, 'bold'))
            canvas1.create_window(165, 40, window=label2)
            canvas1.update_idletasks()
            canvas1.update()
            time.sleep(1)
            label2.destroy()

button1 = tk.Button(text='Send Text', command=Type_Text)
canvas1.create_window(50, 40, window=button1)
root.mainloop()
