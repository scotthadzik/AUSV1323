class Fault:

	def __init__(self, type):
		self.type = type
		self.on_off_relay = False
		self.short_relay  = False
		self.resist_relay = False
		self.cb_relay = False
		
		if self.type == 'open':
			self.on_off_relay = True
			self.short_relay  = False
			self.resist_relay = False
		
		elif self.type == 'short':
			self.cb_relay = True
			self.on_off_relay = True
			self.short_relay  = True
			self.resist_relay = False
			
		
		elif self.type == 'resist':
			self.on_off_relay = True
			self.short_relay  = False
			self.resist_relay = True


	 