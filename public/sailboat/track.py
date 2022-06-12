import cv2
import sys
from utils import *
from darknet import Darknet
from flask import Flask, Response, render_template

app = Flask(__name__)
cap = cv2.VideoCapture(int(sys.argv[1]))

m = Darknet("cfg/yolov3.cfg")
m.load_weights("weights/yolov3.weights")
class_names = load_class_names("data/coco.names")


@app.route("/")
def index():
    return render_template("index.html")


def generate():
    while True:
        frame = cv2.resize(cap.read()[1], (m.width, m.height))
        boxes = detect_objects(m, frame, .4, .6)
        plot_boxes(frame, boxes, class_names, plot_labels=True)
        encFrame = cv2.imencode(".jpg", cv2.resize(frame, (1024, 600)))[1]
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encFrame) + b'\r\n')


@app.route("/video_feed")
def video_feed():
    return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.run(host="localhost", port="4444", debug=True, threaded=True, use_reloader=False)