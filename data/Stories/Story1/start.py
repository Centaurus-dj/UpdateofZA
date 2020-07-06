#! /usr/bin/env python3
# -*- coding: utf-8 -*-

##Imports

import tkinter as tk
print("Tkinter module is imported")
import time
print("Time module is imported")
import os
print("OS module is imported")
import sys
print("Sys module is imported")

##Importation of File path
sys.path.insert(0, '/data')
from data import funcs
print("Function file is imported")

##Importation of readline
import rlcompleter, readline
readline.parse_and_bind('tab: complete')
print("Rlcompleter and Readline modules are imported")


##functions
def phase1():
	header.grid_forget()
	txt1.grid_forget()
	startbutton.grid_forget()
	txt2.grid(row=1, column=2, pady=40, padx=400, sticky=tk.W)
def phase0():
	header.grid(column=1, row=0, pady=12, padx=500)
	txt1.grid(row=1, column=2, sticky=tk.W)
	txt2.grid_forget()

def ToggleFullscreen():
	if root.attributes("-fullscreen") == True:
		print("App is now windowed")
		root.attributes("-fullscreen", False)
		ToggleFullScreen.configure(text="[  ]")
	elif root.attributes("-fullscreen") == False:
		print("App is now in Fullscreen")
		root.attributes("-fullscreen", True)
		ToggleFullScreen.configure(text="[]")


def Quit():
	print("The app is closed... See you next time !")
	root.destroy()

##Creation of the window
print("Creation of the window")
root = tk.Tk()

##Variables of Texts
text1 = ("""  """)
text2 = (""" Test of a text written in a variable for second time """)
Fullscreen_text = "[  ]"





##Title of the window
print("Creation of Window's title")
root.title("Diary of a Survivor")

##Settings of the window
print("We configure the window")
print("We define the size and the background of the window")
root.geometry('1280x720')
root.configure(background="#323232") #We setv the background to dark in hexadecimal

##Header
header = tk.Label(root, text="Diary of a Survivor", bg="#323232", fg="cyan", font=("", 23))
header.grid(column=1, row=0, pady=12, padx=500)

##Text
txt1 = tk.Label(root, text=text1, bg="#323232", fg="#ffffff", font=("", 15))
txt1.grid(row=1, column=1, sticky=tk.W)
txt2 = tk.Label(root, text=text2, bg="#323232", fg="#ffffff", font=("", 15))
txt2.grid_forget()
lbl_space = tk.Label(root, text="", bg="#323232", font=("", 15))
lbl_space.grid(row=2, column=1, sticky=tk.W)

##Buttons
next1 = tk.Button(root, text=">", background="#323232", fg="red", font=("", 23), command=phase1)
next1.grid_forget()
before1 = tk.Button(root, text="<", background="#323232", fg="red", font=("", 23), command=phase0)
before1.grid_forget()
startbutton = tk.Button(root, text="Start", background="#323232", fg="cyan", font=("", 23), command=phase1)
startbutton.grid(row=3, column=1, sticky=tk.W)


#######################################################################
####
###		CREATION OF MAIN BUTTONS, IF YOU WANT TO CHANGE THIS APP AND YOU'RE NOT A GOOD PYTHON PROGRAMMER DON'T 
###		TRY TO CHANGE THE BUTTONS OR INSIDE THEIR CODE !!!!
####
#######################################################################
QuitButton = tk.Button(root, text="X", background="#323232", fg="green", font=("", 23), command=Quit)
QuitButton.grid(row=5, column=1, sticky=tk.W)
ToggleFullScreen = tk.Button(root, text=Fullscreen_text, background="#323232", fg="green", font=("", 23), command=ToggleFullscreen)
ToggleFullScreen.grid(row=6, column=1, sticky=tk.W)



##We launch the window
print("Launching Window....")
root.mainloop()





