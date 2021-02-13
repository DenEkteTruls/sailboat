from electrical import Electrical

class Autopilot:

	def __init__(self):

		self.electrical = Electrical(115200)


	def p5(self):

		self.electrical.set("apilot+5", 1)


	def m5(self):

		self.electrical.set("apilot-5", 1)


	def p1(self):

		self.electrical.set("apilot+1", 1)


	def m1(self):

		self.electrical.set("apilot-1", 1)