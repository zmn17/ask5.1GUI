from tkinter import *
import tkinter.font
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

ledRed = 18
ledGreen = 11
ledBlue = 7

GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledBlue, GPIO.OUT)

## GUI DEFINITIONS ##
win = Tk()
win.title("5.1GUI Task")
win.geometry('350x450+700+200')
myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")


### HELPER FUNCTIONS ###
def toggle_led(led_pin,led_button, button_name):
    led_state = GPIO.input(led_pin)
    if led_state == GPIO.HIGH:
        GPIO.output(led_pin, GPIO.LOW)
        led_button['text'] = f'{button_name} OFF'
    else:
        GPIO.output(led_pin, GPIO.HIGH)
        led_button['text'] = f'{button_name} ON'
        

### EVENT FUNCTIONS ###
def redToggle():
    toggle_led(ledRed,redButton,'RED')

def greenToggle():
    toggle_led(ledGreen, greenButton, 'GREEN')

def blueToggle():
    toggle_led(ledBlue, blueButton, 'BLUE')

def close():
    win.destroy()
    sys.exit()


### WIDGETS ###
redButton = Button(win, text = "RED ON", font = myFont, command = redToggle, bg = "red", height = 1, width = 20)
redButton.grid(row=1, column=1)

greenButton = Button(win, text = "GREEN ON", font = myFont, command = greenToggle, bg = "green", height = 1, width = 20)
greenButton.grid(row=2, column=1)

blueButton = Button(win, text = "BLUE ON", font = myFont, command = blueToggle, bg = "blue", height = 1, width = 20)
blueButton.grid(row=3, column=1)

closeButton = Button(win, text = 'Exit', font = myFont, command = close, height = 2, width = 5)
closeButton.grid(row = 5, column = 1)

win.mainloop()
