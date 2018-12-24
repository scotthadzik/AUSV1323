#!/usr/bin/env python
import LCD1602
import time
import RPi.GPIO as GPIO
from Lesson import Lesson


BtnPin = 11
currentLessonNum = 0
lessonList = []

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.add_event_detect(BtnPin, GPIO.BOTH, callback=detect, bouncetime=200)
	
	LCD1602.init(0x27, 1)	# init(slave address, background light)
	LCD1602.write(0, 0, 'Electrical')
	LCD1602.write(1, 1, 'Trainer')
	time.sleep(2)
	createLessonList()
	
	
def createLessonList():
	global lessonList
	lessonList.append(Lesson(1,'Lesson 1'))
	lessonList.append(Lesson(2,'Lesson 2'))
	lessonList.append(Lesson(3,'Lesson 3'))
	lessonList.append(Lesson(4,'Lesson 4'))
	lessonList.append(Lesson(5,'Lesson 5'))
	lessonList.append(Lesson(6,'Lesson 6'))
	lessonList.append(Lesson(7,'Lesson 7'))
	lessonList.append(Lesson(8,'Lesson 8'))
	lessonList.append(Lesson(9,'Lesson 9'))
	lessonList.append(Lesson(10,'Lesson 10'))
	lessonList.append(Lesson(11,'Lesson 11'))
	lessonList.append(Lesson(12,'Lesson 12'))
	lessonList.append(Lesson(13,'Lesson 13'))


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

def BtnCheck(x):
	global currentLessonNum
	if x == 0:
		currentLessonNum += 1
		setupLab()


def detect(chn):
	BtnCheck(GPIO.input(BtnPin))


def destroy():
	pass	

if __name__ == "__main__":
	try:
		setup()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()