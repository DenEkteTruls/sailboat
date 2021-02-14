
# Author -> Casper Nag (2021)

from electrical import Electrical
import time
import threading
from numba import cuda

class Autopilot:

	def __init__(self, el):

		self.electrical = el
		self.apilot_distance = 0
		self.processing = True
		self.active = False

		self.thread = threading.Thread(target=self.auto, args=())
		self.thread.start()


	def change(self):

		self.active = not self.active


	@cuda.jit(nopython=True)
	def auto(self):

		print("Started autopilotProcessing")

		while self.processing:

			while self.active:

				fives = int(self.apilot_distance/5)
				ones = self.apilot_distance-(fives*5)

				if fives > 0:
					for i in range(fives):
						s_t = time.time()
						if i > 0: self.p5()
						elif i < 0: self.m5()
						while time.time() < st_+2: pass

				elif ones > 0:
					for i in range(ones):
						s_t = time.time()
						if i > 0: self.p1()
						elif i < 0: self.m1()
						while time.time() < st_+2: pass

		print("Ended autopilotProcessing")


	def p5(self):

		self.electrical.set("apilot+5", 1)


	def m5(self):

		self.electrical.set("apilot-5", 1)


	def p1(self):

		self.electrical.set("apilot+1", 1)


	def m1(self):

		self.electrical.set("apilot-1", 1)