from pkg_component.Relay import Relay

class RelayGroup:
	def __init__(self, name, o_pin, s_pin, r_pin):
		self.name = name
		self.on_off_relay = Relay('On Off', o_pin)
		self.short_relay  = Relay('Short', s_pin)
		self.resist_relay = Relay('Resist', r_pin)
		if self.name == 'A1':
			self.on_off_relay.set_relay_number(9)
			self.on_off_relay.set_relay_number(10)
			self.on_off_relay.set_relay_number(11)
		elif self.name == 'A2':
			self.on_off_relay.set_relay_number(13)
			self.on_off_relay.set_relay_number(14)
			self.on_off_relay.set_relay_number(15)
		elif self.name == 'A3':
			self.on_off_relay.set_relay_number(8)
			self.on_off_relay.set_relay_number(7)
			self.on_off_relay.set_relay_number(6)
		elif self.name == 'A4':
			self.on_off_relay.set_relay_number(4)
			self.on_off_relay.set_relay_number(3)
			self.on_off_relay.set_relay_number(2)  