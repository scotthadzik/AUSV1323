

class Relay:

	import RPi.GPIO as GPIO
	
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location


	def __init__ (self, name, relayNumber, outputPin):
		self.name 	= name
		self.relayNumber = relayNumber
		self.outputPin = outputPin

	def toggleRelay(self):
		GPIO.output(self.outputPin, GPIO.LOW)