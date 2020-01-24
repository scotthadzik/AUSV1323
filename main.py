from pkg_tests import testBoard
from pkg_setup import setup_relays
from pkg_setup import setup_faults


def setup():
	relay_dict = setup_relays.createRelayList()
	# testBoard.setup(relay_dict)
	
	fault_dict = setup_faults.create_fault_list()
	
	#set an open in the circuit

	open = fault_dict['open']
	relay = relay_dict['A1_Relays']
	print (open['fault_relay'])
	print (relay.on_off_relay)



	



if __name__ == "__main__":
	try:
		setup()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()   