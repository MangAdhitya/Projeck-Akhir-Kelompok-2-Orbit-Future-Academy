import runpy

import cv

from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# @app.route('/')
# def main():
#     return render_template('baru.html')

# def gen_frames():  # generate frame by frame from camera
#     while True:
#         # Capture frame-by-frame
#         success, frame = 'main.py'.read()  # read the camera frame
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

# main2 = open('main.py')
# camera = cv2.VideoCapture(0)
# camera2 = app.config.from_pyfile('main.py')
# camera3 = cv2.imwrite('main.py', app)
# file = cv2.VideoCapture(runpy.run_module('main.py'))
# def gen_frames():
#     while True:
#         # success, frame = camera.read()  # read the camera frame
#         # success, frame = camera2.read()  # read the camera frame
#         success, frame = file.read()    # read the camera frame
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/')
def index():
    return render_template('jajal.html')

# def run_script():
#     file = open(r'C:\Users\fuadi\Desktop\FILE PENTING\Coba1\main.py', 'r').read()
#     return exec(file)

@app.route('/video_feed')
def video_feed():
    return Response(cv2(runpy.run_module('main.py')).read(), mimetype='multipart/x-mixed-replace; boundary=frame')
    # return Response(index(),
    #                 mimetype='multipart/x-mixed-replace; boundary=frame')

# def gen():
#     """Video streaming generator function."""
#     yield b'--frame\r\n'
#     while True:
#         frame = 'main.py'.get_frame()
#         yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'


# @app.route('/video_feed')
# def video_feed():
#     return Response(index(video_feed),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


    # FLASK_APP = main.py
# @app.route('/video_feed')
# def video_feed():
#     # return app.config.from_pyfile.Response(main('main.py'), 'main.py', mimetype='multipart/x-mixed-replace; boundary=frame')
# # return export FLASK_APP=hello.py
#     FLASK_APP = main.py




if __name__ == '__main__':
    app.run()



# from flask import Flask, render_template, request
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# if __name__ == '__main__':
#     app.run()
