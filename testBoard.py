#!/usr/bin/env python
import LCD1602
import time
import RPi.GPIO as GPIO
from Lesson import Lesson
from Relay import Relay


UPBtnPin = 24
DOWNBtnPin = 26
relayCheckTime = .1
relayList = []
currentLessonNum = 1
lessonList = []
numberOfLessons = 16

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

	setupLab()
	
	
def createLessonList():
	global lessonList
	lessonList.append(Lesson(1,'Lesson 1', 1, True))
	lessonList.append(Lesson(2,'Lesson 2', 2, False))
	lessonList.append(Lesson(3,'Lesson 3', 3, False))
	lessonList.append(Lesson(4,'Lesson 4', 4, False))
	lessonList.append(Lesson(5,'Lesson 5', 5, False))
	lessonList.append(Lesson(6,'Lesson 6', 6, False))
	lessonList.append(Lesson(7,'Lesson 7', 7, False))
	lessonList.append(Lesson(8,'Lesson 8', 8, False))
	lessonList.append(Lesson(9,'Lesson 9', 9, False))
	lessonList.append(Lesson(10,'Lesson 10', 10, False))
	lessonList.append(Lesson(11,'Lesson 11', 11, False))
	lessonList.append(Lesson(12,'Lesson 12', 12, False))
	lessonList.append(Lesson(13,'Lesson 13', 13, False))
	lessonList.append(Lesson(14,'Lesson 14', 14, False))
	lessonList.append(Lesson(15,'Lesson 15', 15, False))
	lessonList.append(Lesson(16,'Lesson 16', 16, False))


def createRelayList():
	LCD1602.write(0, 0, 'Add Relays')
	global relayList
	relayList.append(Relay("Relay 1",1, 11))
	relayList.append(Relay("Relay 2",2, 37))
	relayList.append(Relay("Relay 3",3, 13))
	relayList.append(Relay("Relay 4",4, 12)) 
	relayList.append(Relay("Relay 5",5, 15))
	relayList.append(Relay("Relay 6",6, 16))
	relayList.append(Relay("Relay 7",7, 29))
	relayList.append(Relay("Relay 8",8, 18))
	relayList.append(Relay("Relay 9",9, 31))
	relayList.append(Relay("Relay 10",10, 22))
	relayList.append(Relay("Relay 11",11, 33))
	relayList.append(Relay("Relay 12",12, 32))
	relayList.append(Relay("Relay 13",13, 35))
	relayList.append(Relay("Relay 14",14, 36))
	relayList.append(Relay("Relay 15",15, 40))
	relayList.append(Relay("Relay 16",16, 38))
	
	for relay in relayList:
		GPIO.setup(relay.outputPin, GPIO.OUT, initial=0)
	
def checkRelayBoard():
	LCD1602.write(0, 0, 'Relay Check')
	for relay in relayList:
		LCD1602.write(1, 1, relay.name)
		GPIO.output(relay.outputPin, GPIO.HIGH)
		time.sleep(relayCheckTime)
		GPIO.output(relay.outputPin, GPIO.LOW)
		time.sleep(.5)

def setupLab():
	createRelayList()
	checkRelayBoard()
	createLessonList()
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

def setupPin(lesson):
	GPIO.output(lesson.relay, lesson.status)

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
	print('increase')
	BtnCheck(GPIO.input(UPBtnPin), True)

def decreaseDetect(chn):
	print('decrease')
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