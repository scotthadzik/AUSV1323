from pkg_tests import testBoard
from pkg_setup import setup_relays
from pkg_setup.RelayGroup import RelayGroup
from pkg_setup.Fault import Fault
import time

def setup():
	
	relay_groups = {
	'a1' : RelayGroup('A1',40,35,38),
	'a2' : RelayGroup('A2',37,32,36),
	'a3' : RelayGroup('A3',29,12,22),
	'a4' : RelayGroup('A4',18,13,16)
	}
	# relay_dict = setup_relays.createRelayList()
	# testBoard.setup(relay_dict)
	
	open = Fault('open')
	short = Fault('short')
	resist = Fault('resist')

	fault = open

	for relay_group in relay_groups:
		relay_group.on_off_relay.setRelayStatus(fault.on_off_relay)
		relay_group.short_relay.setRelayStatus(fault.short_relay)
		relay_group.resist_relay.setRelayStatus(fault.resist_relay)
		
		time.sleep(2)

		relay_group.on_off_relay.setRelayStatus(False)
		relay_group.short_relay.setRelayStatus(False)
		relay_group.resist_relay.setRelayStatus(False)

if __name__ == "__main__":
	try:
		setup()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()   