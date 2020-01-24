from pkg_tests import testBoard
from pkg_setup import setup_relays
from pkg_setup.Fault import Fault
import time

def setup():
	relay_dict = setup_relays.createRelayList()
	# testBoard.setup(relay_dict)
	
	open = Fault('open')
	short = Fault('short')
	resist = Fault('resist')

	current_fault = open
	current_relay_set = 'A2_Relays'

	set_of_relays = relay_dict[current_relay_set]

	set_of_relays.on_off_relay.setRelayStatus(current_fault.on_off_relay)
	set_of_relays.short_relay.setRelayStatus(current_fault.short_relay)
	set_of_relays.resist_relay.setRelayStatus(current_fault.resist_relay)

	time.sleep(10)

	set_of_relays.on_off_relay.setRelayStatus(False)
	set_of_relays.short_relay.setRelayStatus(False)
	set_of_relays.resist_relay.setRelayStatus(False)

	current_fault = short
	current_relay_set = 'A3_Relays'

	set_of_relays = relay_dict[current_relay_set]

	set_of_relays.on_off_relay.setRelayStatus(current_fault.on_off_relay)
	set_of_relays.short_relay.setRelayStatus(current_fault.short_relay)
	set_of_relays.resist_relay.setRelayStatus(current_fault.resist_relay)

	time.sleep(10)

	set_of_relays.on_off_relay.setRelayStatus(False)
	set_of_relays.short_relay.setRelayStatus(False)
	set_of_relays.resist_relay.setRelayStatus(False)

	current_fault = resist
	current_relay_set = 'A4_Relays'

	set_of_relays = relay_dict[current_relay_set]

	set_of_relays.on_off_relay.setRelayStatus(current_fault.on_off_relay)
	set_of_relays.short_relay.setRelayStatus(current_fault.short_relay)
	set_of_relays.resist_relay.setRelayStatus(current_fault.resist_relay)

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