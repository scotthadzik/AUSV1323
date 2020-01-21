#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from component_pkg import Relay
from component_pkg import LCD1602

relayCheckTime = 1
relayList = []
currentLessonNum = 1
lessonList = []
numberOfLessons = 16

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	LCD1602.init(0x27, 1)	# init(slave address, background light)
	LCD1602.clear	# init(slave address, background light)
	LCD1602.write(0, 0, 'Electrical')
	LCD1602.write(1, 1, 'Trainer')
	time.sleep(2)
	setupLab()

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

	# ------------relay set A4 ----------------
	relayA4_ON_OFF = Relay("Relay A4 On Off", 4, 18)
	relayA4_Short = Relay("Relay A4 Short", 3, 13)
	relayA4_Resist = Relay("Relay A4 Resist", 2, 16)
	

	relayList.append(relayA1_ON_OFF)
	relayList.append(relayA1_Short)
	relayList.append(relayA1_Resist)
	
	relayList.append(relayA2_ON_OFF)
	relayList.append(relayA2_Short)
	relayList.append(relayA2_Resist)

	relayList.append(relayA3_ON_OFF)
	relayList.append(relayA3_Short)
	relayList.append(relayA3_Resist)

	relayList.append(relayA4_ON_OFF)
	relayList.append(relayA4_Short)
	relayList.append(relayA4_Resist)

	
	for relay in relayList:
		GPIO.setup(relay.outputPin, GPIO.OUT, initial=0)
	
def checkRelayBoard():
	LCD1602.write(0, 0, 'Relay Check')
	for relay in relayList:
		LCD1602.write(1, 1, relay.name)
		relay.setRelayStatus(True)
		time.sleep(relayCheckTime)

def setupLab():
	createRelayList()
	checkRelayBoard()