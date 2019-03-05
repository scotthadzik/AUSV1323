#!/usr/bin/env python
import LCD1602
import time
import RPi.GPIO as GPIO
from Lesson import Lesson
from Relay import Relay


UPBtnPin = 24
DOWNBtnPin = 26
relayList = []
currentLessonNum = 0
lessonList = []
numberOfLessons = 12

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(UPBtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.setup(DOWNBtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.add_event_detect(UPBtnPin, GPIO.BOTH, callback=increaseDetect, bouncetime=500)
	GPIO.add_event_detect(DOWNBtnPin, GPIO.BOTH, callback=decreaseDetect, bouncetime=500)

	
	LCD1602.init(0x27, 1)	# init(slave address, background light)
	LCD1602.clear	# init(slave address, background light)
	LCD1602.write(0, 0, 'Electrical')
	LCD1602.write(1, 1, 'Trainer')
	time.sleep(2)
	createRelayList()
	checkRelayBoard()
	createLessonList()
	
	
def createLessonList():
	global lessonList
	lessonList.append(Lesson(1,'Lesson 1', 40, True))
	lessonList.append(Lesson(2,'Lesson 2', 30, False))
	lessonList.append(Lesson(3,'Lesson 3', 30, False))
	lessonList.append(Lesson(4,'Lesson 4', 30, False))
	lessonList.append(Lesson(5,'Lesson 5', 30, False))
	lessonList.append(Lesson(6,'Lesson 6', 30, False))
	lessonList.append(Lesson(7,'Lesson 7', 30, False))
	lessonList.append(Lesson(8,'Lesson 8', 30, False))
	lessonList.append(Lesson(9,'Lesson 9', 30, False))
	lessonList.append(Lesson(10,'Lesson 10', 30, False))
	lessonList.append(Lesson(11,'Lesson 11', 30, False))
	lessonList.append(Lesson(12,'Lesson 12', 30, False))


def createRelayList():
	LCD1602.write(0, 0, 'Relay Check')
	global relayList
	relayList.append(Relay("Relay 1", 11))
	relayList.append(Relay("Relay 2", 13))
	relayList.append(Relay("Relay 3", 15))
	relayList.append(Relay("Relay 4", 29))
	relayList.append(Relay("Relay 5", 31))
	
	for relay in relayList:
		GPIO.setup(relay.outputPin, GPIO.OUT)
	time.sleep(2)
	

def checkRelayBoard():
	for relay in relayList:
		LCD1602.write(1, 1, relay.name)
		GPIO.output(relay.outputPin, GPIO.LOW)
		time.sleep(2)
		GPIO.output(relay.outputPin, GPIO.HIGH)
		time.sleep(2)
		

	# RELAY 2Pin 3 Relay Board -> GPIO18
	# Pin 4 Relay Board -> GPIO17
	# Pin 5 Relay Board -> GPIO23
	# Pin 6 Relay Board -> GPIO27
	# Pin 7 Relay Board -> GPIO24
	# Pin 8 Relay Board -> GPIO25
	# Pin 9 Relay Board -> GPIO25
	# Pin 10 Relay Board -> GPIO5
	# Pin 11 Relay Board -> GPIO12
	# Pin 12 Relay Board -> GPIO6
	# Pin 13 Relay Board -> GPIO16
	# Pin 14 Relay Board -> GPIO13
	# Pin 15 Relay Board -> GPIO20
	# Pin 16 Relay Board -> GPIO19
	# Pin 17 Relay Board -> GPIO21
	# Pin 18 Relay Board -> GPIO26





def setupLab():
	currentLesson = ''
	for lesson in lessonList:
		if lesson.number == currentLessonNum:
			currentLesson = lesson
			break

	message = ('Lesson # ' + str(currentLessonNum))
	LCD1602.clear()
	LCD1602.write(0, 0, message)
	LCD1602.write(0, 1, currentLesson.name)
	# setupPin(currentLesson)

# def setupPin(lesson):
# 	GPIO.output(lesson.outputPin, lesson.status)

def BtnCheck(x, increaseLab):
	global currentLessonNum
	if x == 0:
		# for pin in outputPins:
		# 	GPIO.output(pin, GPIO.LOW) 
		if increaseLab:
			if currentLessonNum != numberOfLessons:
				currentLessonNum += 1
		else:
			if currentLessonNum > 1:
				currentLessonNum -= 1
		setupLab()

def increaseDetect(chn):
	BtnCheck(GPIO.input(UPBtnPin), True)

def decreaseDetect(chn):
	BtnCheck(GPIO.input(DOWNBtnPin), False)

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