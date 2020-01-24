class Fault:

	def __init__(self, type):
		self.type = type
		on_off_relay = False
		short_relay  = False
		resist_relay = False
		if self.type == 'open':
			on_off_relay = True
			short_relay  = False
			resist_relay = False
		elif self.type == 'short':
			on_off_relay = True
			short_relay  = False
			resist_relay = True
		elif self.type == 'resist':
			on_off_relay = True
			short_relay  = True
			resist_relay = False


	 