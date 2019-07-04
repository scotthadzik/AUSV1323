import time
from Relay import Relay
from Lesson import Lesson
from Fault import Fault
import RPi.GPIO as GPIO



def setup(): 
	relayB1Fault  = Relay("B1 Fault Relay" , 9, 40)
	relayB1Short  = Relay("B1 Short Relay" , 11, 38)
	relayB1Resist = Relay("B1 Resist Relay", 12, 33)
	relayB1Fault.turnRelayON()
	time.sleep(1)
	relayB1Short.turnRelayON()
	time.sleep(1)
	relayB1Resist.turnRelayON()
	time.sleep(1)

	relayGroupB1 = {
		"relayFault"  : relayB1Fault,
		"relayShort"  : relayB1Short,
		"relayResist" : relayB1Resist
	} 

	noFault			= Fault('No Fault')
	openCircuit		= Fault('Open Circuit'	 , True, False, False)
	shortToGround 	= Fault('Short to Ground', True, True , False)
	highResistance 	= Fault('High Resistance', True, False, True)

	lesson1 = Lesson('lesson1', 1, relayGroupB1, openCircuit)
	lesson1.setupFaultForLesson()



def destroy():
	GPIO.cleanup()
	pass

if __name__ == "__main__":
	try:
		setup()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()