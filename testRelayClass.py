import time
from Relay import Relay
from Lesson import Lesson
import RPi.GPIO as GPIO

def setup(): 
	relayB1 = Relay("Relay B1", 9, 40)
	relayB1.turnRelayON()
	print('relayOn')
	time.sleep(2)

	lesson1 = Lesson('lesson1', 1, relayB1)
	lesson1.showLessonInfo()


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