import time
import RPi.GPIO as GPIO

class Relay:

	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location


	def __init__ (self, name, relayNumber, outputPin):
		
		self.name 	= name
		self.relayNumber = relayNumber
		self.outputPin = outputPin

	def setupRelayPinAsOutput(self):
		time.sleep(.5)
		GPIO.setup(self.outputPin, GPIO.OUT, initial=0)

	def toggleRelay(self):
		time.sleep(0.5)
		GPIO.output(self.outputPin, GPIO.LOW)
		time.sleep(0.5)
		GPIO.output(self.outputPin, GPIO.HIGH)
		