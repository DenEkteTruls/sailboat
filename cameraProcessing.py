import cv2
import numpy as np
import threading
from PIL import Image, ImageTk
from time import sleep
from vidstab import VidStab

stabilizer = VidStab()

class CameraProcessing:

	def __init__(self, camIndex, size):

		self.size = size
		self.camIndex = camIndex
		#self.cap = cv2.VideoCapture(self.camIndex)
		self.cap = cv2.VideoCapture("video2.mp4")
		self.frame = cv2.flip(cv2.resize(cv2.imread("splash.jpeg"), self.size), 1)
		self.frame_ticker = 0

		self.faceCascade = cv2.CascadeClassifier("face.xml")

		self.tracker = cv2.TrackerKCF_create()
		self.roi = (0, 0, 0, 0)
		self.last_roi = (10, 10, 100, 100)
		self.tracing = False
		self.waiting = False
		self.distance = 0
		self.apilot_distance = 0
		
		self.processing = True
		self.thread = threading.Thread(target=self.frameProcessing, args=())
		self.thread.start()

		self.ticker1 = 0
		self.ticker2 = 0


	def get_frame(self):

		while len(self.frame) == 0: print("waiting for image")
		return self.frames


	def trace(self):

		self.waiting = True
		self.roi = cv2.selectROI("Select object to trace", self.frame)
		self.waiting = False
		cv2.destroyAllWindows()

		if self.roi != (0, 0, 0, 0):
			self.tracker = cv2.TrackerKCF_create()
			self.tracker.init(self.frame, self.roi)
			self.tracing = True
			self.ticker1 = 0
			self.ticker2 = 0


	def f(self, x): return -((1/10)*x**3 + (75*x))/500


	def calculate_distance(self):

		self.apilot_distance = int(self.f(self.distance))

		print(self.distance, self.apilot_distance)


	def frameProcessing(self):

		print("Starting frameProcessing")

		while self.processing:

			while self.waiting: pass

			rel, f = self.cap.read()
			if not rel: self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0); continue
			frame = cv2.resize(f, self.size)
			#frame = stabilizer.stabilize_frame(input_frame=frame_, border_size=0)
			temp_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

			# GRID
			#cv2.line(temp_frame, (int(self.size[0]/3), self.size[1]), (int(self.size[0]/3), 0), (255, 0, 0), 1)
			#cv2.line(temp_frame, (int(self.size[0]*0.66), self.size[1]), (int(self.size[0]*0.66), 0), (255, 0, 0), 1)
			#cv2.line(temp_frame, (0, int(self.size[1]/3)), (self.size[0], int(self.size[1]/3)), (255, 0, 0), 1)
			#cv2.line(temp_frame, (0, int(self.size[1]*0.66)), (self.size[0], int(self.size[1]*0.66)), (255, 0, 0), 1)
			cv2.circle(temp_frame, (int(self.size[0]/2), int(self.size[1]/2)), 3, (255, 0, 200), 3)

			if self.tracing:
				available, roi = self.tracker.update(temp_frame)
				self.last_roi = roi
				if available:
					cv2.rectangle(temp_frame, (roi[0], roi[1]),(roi[0]+roi[2], roi[1]+roi[3]),(0, 255, 0), 2)
					cv2.line(temp_frame, (roi[0]+int(roi[2]/2), roi[1]), (roi[0]+int(roi[2]/2), int(self.size[1]/2)), (255, 150, 0), 2)
					cv2.line(temp_frame, ((roi[0]+int(roi[2]/2), int(self.size[1]/2))), (int(self.size[0]/2), int(self.size[1]/2)), (255, 150, 0), 2)

					self.distance = ((int(self.size[0]/2))-(roi[0]+int(roi[2]/2)))/10
					self.calculate_distance()
					cv2.putText(temp_frame, f"{self.apilot_distance}", (int(roi[0]+int(roi[2]/2)), (int(self.size[1]/2)-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

					cv2.putText(temp_frame, "Landmark", (10, self.size[1]-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4)
					self.ticker1 = 0
					self.ticker2 = 0
				else:
					self.ticker1 += 1
					if self.ticker1 >= 200:
						cv2.putText(temp_frame, "Landmark", (10, self.size[1]-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 4)
						self.ticker2 += 1
						if self.ticker2 > 2000:
							self.tracing = False
							self.distance = 0
							self.apilot_distance = 0
					else:
						cv2.rectangle(temp_frame, (self.last_roi[0], self.last_roi[1]),(self.last_roi[0]+self.last_roi[2], self.last_roi[1]+self.last_roi[3]),(0, 255, 0), 2)
						cv2.putText(temp_frame, "Landmark", (10, self.size[1]-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4)

			self.frame = temp_frame
			self.frame_ticker += 1
			#sleep(0.02)

		print("Ended frameProcessing")