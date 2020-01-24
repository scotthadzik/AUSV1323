from pkg_tests import testBoard
from pkg_setup import setup_relays
from pkg_setup import setup_faults
import time

def setup():
	relay_dict = setup_relays.createRelayList()
	# testBoard.setup(relay_dict)
	
	fault_dict = setup_faults.create_fault_list()
	
	#set an open in the circuit

	# open = fault_dict['open']
	# short = fault_dict['short']
	# hi_resist = fault_dict['hi_resist']

	
	# print (open['fault_relay'])
	# print (relay.on_off_relay.turnRelayON())

	current_fault = 'open'
	current_relay_set = 'A1_Relays'

	set_of_relays = relay_dict[current_relay_set]
	fault_settings = fault_dict[current_fault]

	set_of_relays.on_off_relay.setRelayStatus(fault_settings['on_off_relay'])
	set_of_relays.short_relay.setRelayStatus(fault_settings['short_relay'])
	set_of_relays.resist_relay.setRelayStatus(fault_settings['resist_relay'])

	time.sleep(10)

	set_of_relays.on_off_relay.setRelayStatus(fault_settings[False])
	set_of_relays.short_relay.setRelayStatus(fault_settings[False])
	set_of_relays.resist_relay.setRelayStatus(fault_settings[False])

def destroy():
	

if __name__ == "__main__":
	try:
		setup()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()   