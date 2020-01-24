from pkg_component.Relay import Relay

class RelayGroup:
	def __init__(self, name, o_pin, s_pin, r_pin):
		self.name = name
		self.on_off_relay = Relay('On Off', 9,o_pin)
		self.short_relay  = Relay('On Off', 10,s_pin)
		self.resist_relay = Relay('On Off', 11,r_pin)