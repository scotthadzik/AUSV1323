import time
from Relay import Relay
from Lesson import Lesson
from Fault import Fault
import RPi.GPIO as GPIO



def setup(): 
	relayB1Fault  = Relay("B1 Fault Relay" , 9, 40)
	relayB1Short  = Relay("B1 Short Relay" , 10, 33) #35 on pcb
	relayB1Resist = Relay("B1 Resist Relay", 11, 38)
	

	relayGroupB1 = {
		"faultRelay"  : relayB1Fault,
		"shortRelay"  : relayB1Short,
		"resistRelay" : relayB1Resist
	} 

	noFault			= Fault('No Fault')
	openCircuit		= Fault('Open Circuit'	 , True, False, False)
	shortToGround 	= Fault('Short to Ground', True, True , False)
	highResistance 	= Fault('High Resistance', True, False, True)

	lesson1 = Lesson('lesson1', 1, relayGroupB1, openCircuit)
	time.sleep(2)
	lesson1 = Lesson('lesson1', 1, relayGroupB1, shortToGround)
	time.sleep(2)
	lesson1 = Lesson('lesson1', 1, relayGroupB1, highResistance)
	time.sleep(2)
	lesson1 = Lesson('lesson1', 1, relayGroupB1, noFault)


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