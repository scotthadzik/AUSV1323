import Relay

class Lesson:

	def __init__ (self, name, number, relay):
		self.name 	= name
		self.number = number
		self.relay = relay

	def showLessonInfo(self):
		print(self.name)
		print(self.number)
		print(self.relay.name)