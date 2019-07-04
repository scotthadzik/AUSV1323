import Relay

class Lesson:

	def __init__ (self, name, number, relayGroup, fault):
		self.name 	= name
		self.number = number
		self.relayGroup = relayGroup
		self.fault = fault

	def showLessonInfo(self):
		print(self.name)
		print(self.number)

	def setupFaultForLesson(self):
		print(self.name)
		faultRelay = 	self.relayGroup["faultRelay"]
		shortRelay = 	self.relayGroup["shortRelay"]
		resistRelay = 	self.relayGroup["resistRelay"]
		faultRelay.setRelayStatus(self.fault.faultRelay)
		shortRelay.setRelayStatus(self.fault.shortRelay)
		resistRelay.setRelayStatus(self.fault.resistRelay)
		print (faultRelay.name)
		print (shortRelay.name)
		print (resistRelay.name)
		