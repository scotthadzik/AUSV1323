import time
from Relay import Relay

relayB1 = Relay("Relay B1", 9, 40)
print('relayOn')
relayB1.turnRelayON()
time.sleep(.5)
print('relayOFF')
relayB1.turnRelayOFF()
time.sleep(.5)