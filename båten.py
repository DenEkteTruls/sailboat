import cv2
import numpy as np
import tkinter as tk
from electrical import Electrical
from autopilot import Autopilot
from PIL import Image, ImageTk
import threading

cap = cv2.VideoCapture(0)
frame_buffer = None

electrical = Electrical(115200)
autopilot = Autopilot()

window = tk.Tk()
window.title = "Seilbåtkontroller'n"
window.geometry("800x380")
window.bind('<Escape>', lambda e: window.quit())

apilot = tk.Frame(window, highlightthickness=1, highlightbackground="black")
apilot_title = tk.Label(apilot, text="Autopilot", width=8)
apilot_p5 = tk.Button(apilot, text="+5", width=8)#, callback=autopilot.p5())
apilot_m5 = tk.Button(apilot, text="-5", width=8)#, callback=autopilot.m5())
apilot_p1 = tk.Button(apilot, text="+1", width=8)#, callback=autopilot.p1())
apilot_m1 = tk.Button(apilot, text="-1", width=8)#, callback=autopilot.m5())
apilot_title.pack()
apilot_m1.pack(); apilot_p1.pack()
apilot_m5.pack(); apilot_p5.pack()
apilot.place(x=10, y=10)

lights = tk.Frame(window, highlightthickness=1, highlightbackground="black")
lights_title = tk.Label(lights, text="Lightcontroll", width=12)
livingroom_lights = tk.Button(lights, text="Stue", width=12)
bedroom_lights = tk.Button(lights, text="Soverom", width=12)
bathroom_lights = tk.Button(lights, text="Dass", width=12)
lanterner = tk.Button(lights, text="Lanterner", width=12)
lights_title.pack()
livingroom_lights.pack(); bedroom_lights.pack()
bathroom_lights.pack(); lanterner.pack()
lights.place(x=10, y=160)

def show_frame():
	while True:

		frame = cv2.flip(cv2.resize(cap.read()[1], (640, 360)), 1)
		cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
		image = Image.fromarray(cv2img)
		imgtk = ImageTk.PhotoImage(image)
		frame_buffer = imgtk

threading._start_new_thread(show_frame, ())


camera = tk.Frame(window, highlightthickness=1, highlightbackground="black", width=640, height=360)

lmain = tk.Label(camera)
lmain.pack()

lmain.imgtk = frame_buffer
lmain.configure(image=frame_buffer)
lmain.after(10, show_frame)

camera.place(x=150, y=10)

window.mainloop()
