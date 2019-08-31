import RPi.GPIO as GPIO
outputPin = 40

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(outputPin, GPIO.OUT, initial=0)
	GPIO.output(outputPin, GPIO.HIGH)
