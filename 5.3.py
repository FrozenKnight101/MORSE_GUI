from tkinter import * 
import tkinter.font 
from gpiozero import LED 
import RPi.GPIO as GPIO
import time

blue = LED(23)

win = Tk() 
win.title("MORSE GUI via LED")
win.geometry('250x150')
myFont = (tkinter.font.Font(family = 'Helvetica', size=15, weight="bold" ))

GPIO.setmode(GPIO.BCM)

def long_Blink():
    blue.on()
    time.sleep(1.5)
    blue.off()
    time.sleep(0.25)

def short_Blink():
    blue.on()
    time.sleep(0.25)
    blue.off()
    time.sleep(0.25)

def morsecode(letter):
    if(letter == "A" or letter == "a"): 
        short_Blink()
        long_Blink()
    elif (letter == "B" or letter == "b"):
        long_Blink()
        short_Blink()
        short_Blink()
        short_Blink()
    elif (letter == "C" or letter == "c"): 
        long_Blink()
        short_Blink()
        long_Blink()
        shortBlink()
    elif (letter == "D" or letter == "d"):
        long_Blink()
        short_Blink()
        short_Blink()
    elif (letter == "E" or letter == "e"): 
        short_Blink()
    elif (letter == "F" or letter == "f"): 
        short_Blink()
        short_Blink()
        long_Blink()
        short_Blink()
    elif (letter == "G" or letter == "g"): 
        long_Blink()
        long_Blink()
        short_Blink()
    elif (letter == "H" or letter == "h"): 
        short_Blink()
        short_Blink()
        short_Blink()
        short_Blink()
    elif (letter == "I" or letter == "i"): 
        short_Blink()
        short_Blink()
    elif (letter == "J" or letter == "j"): 
        short_Blink()
        long_Blink()
        long_Blink()
        long_Blink()
    elif (letter == "K" or letter == "k"): 
        long_Blink()
        short_Blink()
        long_Blink()
    elif (letter == "L" or letter == "l"): 
        short_Blink()
        long_Blink()
        short_Blink()
        short_Blink()
    elif (letter == "M" or letter == "m"):
        long_Blink()
        long_Blink()
    elif (letter == "N" or letter == "n"): 
        long_Blink()
        short_Blink()
    elif (letter == "O" or letter == "o"): 
        long_Blink()
        long_Blink()
        long_Blink()
    elif (letter == "P" or letter == "p"): 
        short_Blink()
        long_Blink()
        long_Blink()
        short_Blink()  
    elif (letter == "Q" or letter == "q"): 
        long_Blink()
        long_Blink()
        short_Blink()
        long_Blink()
    elif (letter == "R" or letter == "r"): 
        short_Blink()
        long_Blink()
        short_Blink()
    elif (letter == "S" or letter == "s"): 
        short_Blink()
        short_Blink()
        short_Blink()
    elif (letter == "T" or letter == "t"): 
        long_Blink()
    elif (letter == "U" or letter == "u"):
        short_Blink()
        short_Blink()
        long_Blink()
    elif (letter == "V" or letter == "v"): 
        short_Blink()
        short_Blink()
        short_Blink()       
        long_Blink()
    elif (letter == "W" or letter == "w"): 
        short_Blink()
        long_Blink()
        long_Blink()        
    elif (letter == "X" or letter == "x"): 
        long_Blink()       
        short_Blink()
        short_Blink()
        long_Blink()
    elif (letter == "Y" or letter == "y"): 
        long_Blink()       
        short_Blink()
        long_Blink()
        long_Blink()        
    elif (letter == "Z" or letter == "z"): 
        long_Blink()       
        long_Blink()
        short_Blink()
        short_Blink()        
    else:  
        lab.config(text = "Invalid")  

def text_morse():
    i = inputtxt.get( );
    if (len(i) <= 12): 
        lab.config(font=myFont, text = "Input: " + i + "   Length: " + str(len(i)))
        j=0  
        while True: 
            if(j < len(i) ):
                morsecode(i[j]) 
                j=j+1
    else:
        lab.config(text = "Max 12 Characters Only") 
            
  
inputtxt = Entry(win, width = 25); 
inputtxt.pack()

convert_Button = Button(win, font=myFont, text= "Morse Conversion", command = text_morse, bg= 'blue', height = 2, width=25) 
convert_Button.pack()
lab = Label(win, text="")
lab.pack()

win.mainloop() 
