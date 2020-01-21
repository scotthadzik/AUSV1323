#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from pkg_component.Relay import Relay
from pkg_component import LCD1602

relayCheckTime = 1

def setup(relayList):
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	LCD1602.init(0x27, 1)	# init(slave address, background light)
	LCD1602.clear	# init(slave address, background light)
	LCD1602.write(0, 0, 'Relay')
	LCD1602.write(1, 1, 'Check')
	time.sleep(2)
	
	for relay in relayList:
		GPIO.setup(relay.outputPin, GPIO.OUT, initial=0)
	
	cycle_relays(relayList, True)
	cycle_relays(relayList, False)

def cycle_relays(relayList, state):
	for relay in relayList:
		LCD1602.write(1, 1, relay.name)
		relay.setRelayStatus(state)
		time.sleep(relayCheckTime)
	
	

