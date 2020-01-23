from pkg_component.Relay import Relay
from pkg_component.RelaySet import RelaySet

def createRelayList():
	
	relay_dict = {

		'A1_Relays' : RelaySet(
			'relayA1', 
			Relay("Relay A1 On Off", 9, 40),
			Relay("Relay A1 Short", 10, 35),
			Relay("Relay A1 Resist", 11, 38)),
		'A2_Relays' : RelaySet(
			'relayA2', 
			Relay("Relay A2 On Off", 13, 37),
			Relay("Relay A2 Short", 14, 32),
			Relay("Relay A2 Resist", 15, 36)),
		'A3_Relays' : RelaySet(
			'relayA3', 
			Relay("Relay A3 On Off", 8, 29),
			Relay("Relay A3 Short", 7, 12),
			Relay("Relay A3 Resist", 6, 22)),
		'A4_Relays' : RelaySet(
			'relayA4', 
			Relay("Relay A4 On Off", 4, 18),
			Relay("Relay A4 Short", 3, 13),
			Relay("Relay A4 Resist", 2, 16))
	}

	return relay_dict
