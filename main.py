from pkg_tests import testBoard
from pkg_setup import setup_relays
from pkg_setup.Faults import Faults
import time

def setup():
	relay_dict = setup_relays.createRelayList()
	# testBoard.setup(relay_dict)
	
	open = Fault('open')
	short = Fault('short')
	resist = Fault('resist')

	current_fault = open
	current_relay_set = 'A1_Relays'

	set_of_relays = relay_dict[current_relay_set]

	set_of_relays.on_off_relay.setRelayStatus(fault.on_off_relay)
	set_of_relays.short_relay.setRelayStatus(fault_settings['short_relay'])
	set_of_relays.resist_relay.setRelayStatus(fault_settings['resist_relay'])

	time.sleep(10)

	set_of_relays.on_off_relay.setRelayStatus(False)
	set_of_relays.short_relay.setRelayStatus(False)
	set_of_relays.resist_relay.setRelayStatus(False)

if __name__ == "__main__":
	try:
		setup()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()   