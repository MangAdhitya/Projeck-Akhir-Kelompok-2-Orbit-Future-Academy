# import cv2
# import pickle
# import cvzone
# import numpy as np
#
# cap = cv2.VideoCapture('carPark.mp4')
#
# with open('CarApaAja', 'rb') as f:
#     posList = pickle.load(f)
#
# width, height = 107, 48
#
# def checkParkingSpace(imgPro):
#     spaceCounter = 0
#
#     for pos in posList:
#         x, y = pos
#
#         imgCrop = imgPro[y:y + height, x:x + width]
#
#         count = cv2.countNonZero(imgCrop)
#
#
#         if count < 900:
#             color = (0, 255, 0)
#             thickness = 1
#             spaceCounter += 1
#         else:
#             color = (0, 0, 255)
#             thickness = 1
#
#         cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
#         cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, thickness=1, offset=10, colorR=color)
#
#     cvzone.putTextRect(img, f'Parkir Kosong: {spaceCounter} dari {len(posList)}', (100,50), scale=3, thickness=1, offset=10, colorR=(0,200,0))
#
# while True:
#
#     if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
#         cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
#     success,img = cap.read()
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
#     imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
#     imgMedian = cv2.medianBlur(imgThreshold, 5)
#     kernel = np.ones((3, 3), np.uint8)
#     imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)
#
#     checkParkingSpace(imgDilate)
#     cv2.imshow("Cari Parkir", img)
#     cv2.waitKey(10)
import runpy
import time
import cv2
from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('jajal.html')


def gen():
    """Video streaming generator function."""

    cap = cv2.VideoCapture('videocar.mp4')

    # Read until video is completed
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, img = cap.read()
        if ret == True:
            img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.1)
        else:
            break


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run()