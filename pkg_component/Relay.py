import time
import RPi.GPIO as GPIO

class Relay:

	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location

	def __init__ (self, name, outputPin, relayState = False):
		
		self.name 	= name
		self.outputPin = outputPin
		self.relayNumber = None
		GPIO.setup(self.outputPin, GPIO.OUT, initial=0)		


	def set_relay_number(self, number):
		self.relayNumber = number

	def setRelayStatus(self, status):
		if status:
			self.turnRelayON()
		else:
			self.turnRelayOFF()
	
	def turnRelayON(self):
		GPIO.output(self.outputPin, GPIO.HIGH)
		
	def turnRelayOFF(self):
		GPIO.output(self.outputPin, GPIO.LOW)
		