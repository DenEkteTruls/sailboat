
# Author -> Casper Nag (2021)

import json
import serial
from pprint import pprint

class Electrical:

	# initializing the electrical component with reading
	# of the pinout data and serial setup.

	def __init__(self, baudrate, data={}):

		self.data = data
		self.baudrate = baudrate
		self.pinout_filename = "pinout.json"

		self.serial = serial.Serial(baudrate=self.baudrate)

		if len(self.data) > 0:
			self.save(self.pinout_filename)
		else:
			self.data = self.read(self.pinout_filename)

		print("PINOUT:"); pprint(self.data)


	# Set a pinout value through serial to microcontroller.

	def set(self, name, value):

		data = f"{self.data[name]}&{value}"
		self.serial.write(data)


	# Receiving the current pin connected to the name.

	def get(self, name) -> int:

		return self.data[name]


	# Saves the json pinout data.

	def save(self, filename):

		with open(filename, "w") as f:
			json.dump(self.data, f)


	# Reads the pinout database.

	def read(self, filename) -> list:

		with open(filename, "r") as f:
			return json.load(f)