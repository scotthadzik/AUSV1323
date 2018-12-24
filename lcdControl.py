#!/usr/bin/env python
import LCD1602
import time
import RPi.GPIO as GPIO


BtnPin = 11
currentLesson = 0


def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.add_event_detect(BtnPin, GPIO.BOTH, callback=detect, bouncetime=200)
	
	LCD1602.init(0x27, 1)	# init(slave address, background light)
	LCD1602.write(0, 0, 'Greetings!!')
	LCD1602.write(1, 1, 'from SunFounder')
	time.sleep(2)

def Print(x):
	if x == 0:
		print ('    ***********************')
		print ('    *   Button Pressed!   *')
		print ('    ***********************')
		currentLesson =+ 1
		print ('current lesson' + str(currentLesson))

def detect(chn):
	Print(GPIO.input(BtnPin))


def loop():
	space = '                '
	greetings = 'Thank you for buying SunFounder Sensor Kit for Raspberry! ^_^'
	greetings = space + greetings
	while True:
		tmp = greetings
		for i in range(0, len(greetings)):
			LCD1602.write(0, 0, tmp)
			tmp = tmp[1:]
			time.sleep(0.8)
			LCD1602.clear()

def destroy():
	pass	

if __name__ == "__main__":
	try:
		setup()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()