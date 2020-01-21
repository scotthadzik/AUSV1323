from test_pkg import testBoard


def setup():
        testBoard.setup()

if __name__ == "__main__":
	try:
		setup()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()   