from tkinter import filedialog
from tkinter import *
import sys
import os
import shutil
from PIL import Image, ImageFile
import io
import pathlib



def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    #print(folder_path)
    #print(filename)


    
def conv():
    print("\n TIFF to JPG Conversion - 300 DPI \n")
    print("\n Developed by A Rajasekaran\n")
    print("\n Date: 22 April 2022 \n\n")
    f1 = os.listdir(filename) 
    for fname in os.listdir(filename):
        #print(fname)
        if not fname.endswith(".tif"):
            #print(fname)
            continue
        test = os.path.splitext(fname)[0]
        #print(test)
        value1 = filename + '/' + fname
        #print(value1)

        image = Image.open(value1)
        name1 = filename + '/' + test + ".jpg"
        print(name1)
        image.save(name1, 'jpeg', dpi=(300,300), quality=90)
    messagebox.showinfo("TIFF to JPG", "Completed")
    #print(filename)
    
root = Tk()
root.geometry("400x250")
root.config(bg='#ffcc00') 

folder_path = StringVar()
label_value = 'TIFF to JPG Conversion - 300 DPI'
lbl1 = Label(root, text='TIFF to JPG Conversion - 300 DPI', font='helvetica 15', bg='#ffcc00')
lbl1.pack(pady=10)
button2 = Button(text="Browse", command=browse_button, bg='royalblue', fg = 'white').pack(pady=25)
button3 = Button(text="Submit", command=conv, bg='royalblue', fg = 'white').pack(pady=25)
lbl2 = Label(root, textvariable=folder_path, font='helvetica 12', bg='#ffcc00')
lbl2.pack(pady=10)



mainloop()


