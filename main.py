from pkg_tests import testBoard
from pkg_setup import setup_relays
from pkg_setup import setup_faults


def setup():
	relayList = setup_relays.createRelayList()
	testBoard.setup(relayList)
	
	faultList = setup_faults.create_fault_list()
	print (faultList)

if __name__ == "__main__":
	try:
		setup()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()   