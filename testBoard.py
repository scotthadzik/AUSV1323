#!/usr/bin/env python
import LCD1602
import time
import RPi.GPIO as GPIO
from Lesson import Lesson
from Relay import Relay


UPBtnPin = 24
DOWNBtnPin = 26
relayCheckTime = 1
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

	# 2:16, 3:13, 4:18,  ,  6:22, 7:12, 8:29, 9:40, 10:35, 11:38, 13:33, 14:15, 15:11

	# ------------relay set A1 ----------------
	relayA1_ON_OFF = Relay("Relay A1 On Off", 9, 40)
	relayA1_Short = Relay("Relay A1 Short", 10, 35)
	relayA1_Resist = Relay("Relay A1 Resist", 11, 38)
	
	# ------------relay set A2 ----------------
	relayA2_ON_OFF = Relay("Relay A2 On Off", 13, 37)
	relayA2_Short = Relay("Relay A2 Short", 14, 32)
	relayA2_Resist = Relay("Relay A2 Resist", 15, 36)

	# ------------relay set A3 ----------------
	relayA3_ON_OFF = Relay("Relay A3 On Off", 8, 29)
	relayA3_Short = Relay("Relay A3 Short", 7, 12)
	relayA3_Resist = Relay("Relay A3 Resist", 6, 22)
	

	relayList.append(relayA1_ON_OFF)
	relayList.append(relayA1_Short)
	relayList.append(relayA1_Resist)
	
	relayList.append(relayA2_ON_OFF)
	relayList.append(relayA2_Short)
	relayList.append(relayA2_Resist)

	relayList.append(relayA3_ON_OFF)
	relayList.append(relayA3_Short)
	relayList.append(relayA3_Resist)

	
	for relay in relayList:
		GPIO.setup(relay.outputPin, GPIO.OUT, initial=0)
	
def checkRelayBoard():
	LCD1602.write(0, 0, 'Relay Check')
	for relay in relayList:
		LCD1602.write(1, 1, relay.name)
		relay.setRelayStatus(True)
		time.sleep(relayCheckTime)
		# relay.setRelayStatus(False)
		# time.sleep(relayCheckTime)

def setupLab():
	createRelayList()
	checkRelayBoard()
	# createLessonList()
	# currentLesson = ''
	# for lesson in lessonList:
	# 	if lesson.number == currentLessonNum:
	# 		currentLesson = lesson
	# 		break

	# message = ('Lesson # ' + str(currentLessonNum))
	# LCD1602.clear()
	# LCD1602.write(0, 0, message)
	# LCD1602.write(0, 1, currentLesson.name)
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