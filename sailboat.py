
# Author -> Casper Nag (2021)

import cv2
import numpy as np
import tkinter as tk
from electrical import Electrical
from autopilot import Autopilot
from cameraProcessing import CameraProcessing
from PIL import Image, ImageTk
import threading

size = (1280, 720)
cameraProcessing = CameraProcessing(0,size)

electrical = Electrical(115200, {
	"depth": 1,
	"speed": 2,
	"lanterne": 3,
	"apilot-1": 10,
	"apilot+1": 11,
	"apilot-5": 12,
	"apilot+5": 13
	})

autopilot = Autopilot(electrical)

window = tk.Tk()
window.geometry(f"{size[0]+200}x{size[1]+20}")

apilot = tk.Frame(window, highlightthickness=1, highlightbackground="black")
apilot_title = tk.Label(apilot, text="Autopilot", width=8, font=('​Helvetica', 18, 'bold'))
apilot_on_off = tk.Button(apilot, text="AUTO", width=8, command=lambda:autopilot.change())
apilot_p5 = tk.Button(apilot, text="+5", width=8, command=lambda:autopilot.p5())
apilot_m5 = tk.Button(apilot, text="-5", width=8, command=lambda:autopilot.m5())
apilot_p1 = tk.Button(apilot, text="+1", width=8, command=lambda:autopilot.p1())
apilot_m1 = tk.Button(apilot, text="-1", width=8, command=lambda:autopilot.m5())
apilot_title.pack(); apilot_on_off.pack(pady=2)
apilot_m1.pack(pady=2); apilot_p1.pack(pady=2)
apilot_m5.pack(pady=2); apilot_p5.pack(pady=5)
apilot.place(x=10, y=10)

lights = tk.Frame(window, highlightthickness=1, highlightbackground="black")
lights_title = tk.Label(lights, text="Lightcontroll", width=10, font=('​Helvetica', 18, 'bold'))
livingroom_lights = tk.Button(lights, text="Stue", width=10)
bedroom_lights = tk.Button(lights, text="Soverom", width=10)
bathroom_lights = tk.Button(lights, text="Dass", width=10)
lanterner = tk.Button(lights, text="Lanterner", width=10)
lights_title.pack()
livingroom_lights.pack(pady=2); bedroom_lights.pack(pady=2)
bathroom_lights.pack(pady=2); lanterner.pack(pady=5)
lights.place(x=10, y=220)

camera = tk.Frame(window, highlightthickness=1, highlightbackground="black")
lmain = tk.Label(camera)
lmain.bind("<Button-1>", lambda e: cameraProcessing.trace())
lmain.pack()

def show_frame():

	img = Image.fromarray(cameraProcessing.frame)
	imgtk = ImageTk.PhotoImage(image=img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, show_frame)

show_frame()
camera.place(x=190, y=10)

autopilot.apilot_distance = cameraProcessing.apilot_distance

window.mainloop()
cameraProcessing.processing = False
autopilot.processing = False