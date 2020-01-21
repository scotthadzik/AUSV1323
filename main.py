from pkg_tests import testBoard
from pkg_setup import setup_relays


def setup():
	relayList = setup_relays.createRelayList()
	testBoard.setup(relayList)

if __name__ == "__main__":
	try:
		setup()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()   