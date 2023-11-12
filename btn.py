from gpiozero import Button
from signal import pause
import os

button1 = Button(26)
button2 = Button(4)
button3 = Button(21)
button4 = Button(17)
button5 = Button(20)
button6 = Button(18)

def when_b1_pressed():
        print("Button1 pressed!")
        os.system("python3 print.py /dev/ttyUSB0 FANUC-PPR/makerfaire.txt shape")

def when_b2_pressed():
        print("Button2 pressed!")
        os.system("python3 print.py /dev/ttyUSB0 FANUC-PPR/szdiy.txt shape")

def when_b3_pressed():
	print("Button3 pressed!")
	os.system("python3 print.py /dev/ttyUSB0 FANUC-PPR/thematrix.txt bin")

def when_b4_pressed():
	print("Button4 pressed!")
	os.system("python3 print.py /dev/ttyUSB0 FANUC-PPR/bladerunner.txt bin")


def when_b5_pressed():
	print("Button5 pressed!")
	os.system("python3 print.py /dev/ttyUSB0 FANUC-PPR/rickandmorty.txt bin")

def when_b6_pressed():
        print("Button6 pressed!")
        os.system("python3 FANUC-PPR/type.py /dev/ttyUSB0")


button1.when_pressed = when_b1_pressed
button2.when_pressed = when_b2_pressed
button3.when_pressed = when_b3_pressed
button4.when_pressed = when_b4_pressed
button5.when_pressed = when_b5_pressed
button6.when_pressed = when_b6_pressed

pause() 
