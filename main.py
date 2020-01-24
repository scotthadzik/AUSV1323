from pkg_tests import testBoard
from pkg_setup import setup_relays
from pkg_setup.RelayGroup import RelayGroup
from pkg_setup.Fault import Fault
import time

def setup():
	
	a1 = RelayGroup('A1',40,35,38)
	a2 = RelayGroup('A2',37,32,36)
	a3 = RelayGroup('A3',29,12,22)
	a4 = RelayGroup('A4',18,13,16)
	
	# relay_dict = setup_relays.createRelayList()
	# testBoard.setup(relay_dict)
	
	open = Fault('open')
	short = Fault('short')
	resist = Fault('resist')

	fault = open

	# set_of_relays = relay_dict[current_relay_set]
	print ('on off relay num',a1.on_off_relay.relayNumber)
	print ('on off relay num',a1.name)
	a1.on_off_relay.setRelayStatus(fault.on_off_relay)
	a1.short_relay.setRelayStatus(fault.short_relay)
	a1.resist_relay.setRelayStatus(fault.resist_relay)

	time.sleep(10)

	a1.on_off_relay.setRelayStatus(False)
	a1.short_relay.setRelayStatus(False)
	a1.resist_relay.setRelayStatus(False)

if __name__ == "__main__":
	try:
		setup()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()   