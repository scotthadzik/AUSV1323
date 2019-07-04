import time
from Relay import Relay
from Lesson import Lesson

relayB1 = Relay("Relay B1", 9, 40)
print('relayOn')

lesson1 = Lesson('lesson1', 1, relayB1)