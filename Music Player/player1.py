# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 01:02:42 2019

@author: mankup
"""

import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import Label
from mutagen.id3 import ID3

root = Tk()
root.minsize(300,300)

listofsongs = []
index = 0
real_names = []
v = StringVar()
songlabel = Label(root,textvariable = v, width = 35)

def nextsong(event):
    global index
    index +=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def prevsong(event):
    global index
    index -=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    #return songname
 
def updatelabel():
    global index
    global songname
    v.set(real_names[index])
    return songname
    

def directorychooser():
    directory = askdirectory()
    os.chdir(directory)
    
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)
            audio = ID3(realdir) #get meta data of data
            real_names.append(audio["TIT2"].text[0]) #returns title
            listofsongs.append(files)
    
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
    
label = Label(root,text='Music Player')
label.pack()

listbox = Listbox(root)
listbox.pack()

real_names.reverse()
for items in listofsongs:
    listbox.insert(0,items)
real_names.reverse()

nextbutton = Button(root,text='Next song')
nextbutton.pack()
nextbutton.bind("<Button-1>",nextsong)

previousbutton = Button(root,text='Previous song')
previousbutton.pack()
previousbutton.bind("<Button-1>",prevsong)

stopbutton = Button(root,text='Stop')
stopbutton.pack()
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()

directorychooser()
    
root.mainloop()