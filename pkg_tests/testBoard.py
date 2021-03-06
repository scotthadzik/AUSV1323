#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from pkg_component.Relay import Relay
from pkg_component.RelaySet import RelaySet
from pkg_component import LCD1602

relayCheckTime = 1

def setup(relay_dict):
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	LCD1602.init(0x27, 1)	# init(slave address, background light)
	LCD1602.clear	# init(slave address, background light)
	LCD1602.write(0, 0, 'Relay')
	LCD1602.write(1, 1, 'Check')
	time.sleep(2)
	
	for value in relay_dict.values():
		GPIO.setup(value.on_off_relay.outputPin, GPIO.OUT, initial=0)
		GPIO.setup(value.short_relay.outputPin, GPIO.OUT, initial=0)
		GPIO.setup(value.resist_relay.outputPin, GPIO.OUT, initial=0)
	
	cycle_relays(relay_dict, True)
	cycle_relays(relay_dict, False)

def cycle_relays(relay_dict, state):
	for relay_set in relay_dict.values():
		relay_set.on_off_relay.setRelayStatus(state)
		relay_set.short_relay.setRelayStatus(state)
		relay_set.resist_relay.setRelayStatus(state)
		time.sleep(relayCheckTime)
	
	

