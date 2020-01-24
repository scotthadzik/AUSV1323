from pkg_tests import testBoard
from pkg_setup import setup_relays
from pkg_setup import setup_faults


def setup():
	relay_dict = setup_relays.createRelayList()
	# testBoard.setup(relay_dict)
	
	fault_dict = setup_faults.create_fault_list()
	
	#set an open in the circuit

	# open = fault_dict['open']
	# short = fault_dict['short']
	# hi_resist = fault_dict['hi_resist']

	set_of_relays = relay_dict['A1_Relays']
	# print (open['fault_relay'])
	# print (relay.on_off_relay.turnRelayON())

	current_fault = 'open'

	fault_settings = fault_dict[current_fault]

	set_of_relays.on_off_relay.setRelayStatus(fault_settings['on_off_relay'])
	set_of_relays.short_relay.setRelayStatus(fault_settings['short_relay'])
	set_of_relays.resist.setRelayStatus(fault_settings['resist_relay'])




	



if __name__ == "__main__":
	try:
		setup()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()   