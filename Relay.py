import time
import RPi.GPIO as GPIO

class Relay:

	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location


	def __init__ (self, name, relayNumber, outputPin, relayState = False):
		
		self.name 	= name
		self.relayNumber = relayNumber
		self.outputPin = outputPin
		GPIO.setup(self.outputPin, GPIO.OUT, initial=0)		

	def turnRelayON(self):
		GPIO.output(self.outputPin, GPIO.HIGH)
		
		
	def turnRelayOFF(self):
		GPIO.output(self.outputPin, GPIO.LOW)
		
		
		