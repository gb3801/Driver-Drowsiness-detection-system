from flask import Flask, jsonify
from threading import Thread
from imutils import face_utils
import dlib
import cv2
from pygame import mixer
import threading
import sys

thres = 6

mixer.init()
sound = mixer.Sound('sound file\\alarm.wav')

dlist = []

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

def dist(a,b):
    x1,y1 = a
    x2,y2 = b
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

# Define a flag variable to stop the detection loop
detection_running = False

def detect_faces():
    global detection_running

    while detection_running:
        # Getting out image by webcam 
        _, image = cap.read()
        # Converting the image to gray scale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Get faces into webcam's image
        rects = detector(gray, 0)

        # For each detected face, find the landmark.
        for (i, rect) in enumerate(rects):
            # Make the prediction and transform it to numpy array
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            # Draw on our image, all the finded coordinate points (x,y) 
            for (x, y) in shape:
                cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

            le_38 = shape[37]
            le_39 = shape[38]
            le_41 = shape[40]
            le_42 = shape[41]

            re_44 = shape[43]
            re_45 = shape[44]
            re_47 = shape[46]
            re_48 = shape[47]

            dlist.append((dist(le_38,le_42)+dist(le_39,le_41)+dist(re_44,re_48)+dist(re_45,re_47))/4<thres)
            if len(dlist)>10:
                dlist.pop(0)

            # Drowsiness detected
            if sum(dlist)>=4:
                try:
                    sound.play()
                    cv2.putText(image, "ALERT: Drowsiness detected! Wake Up plz", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                except:
                    pass
            else:
                try:
                    sound.stop()
                except:
                    pass

        # Show the image
        cv2.putText(image, "Press 'q' to exit", (10, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow("Output", image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

from flask import Flask, jsonify, render_template
from threading import Thread

app = Flask(__name__)

# Define a flag variable to stop the detection loop
detection_running = False

# Define a function to start the detection loop
def start_detection():
    global detection_running
    detection_running = True
    detect_faces()

# Define a function to stop the detection loop
'''def stop_detection():
    global detection_running
    detection_running = False'''

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start')
def start():
    # Start a new thread to run the detection loop
    thread = Thread(target=start_detection)
    thread.start()
    return jsonify({'message': 'Detection loop started successfully!'})

'''@app.route('/stop')
def stop():
    # Stop the detection loop
    stop_detection()
    return jsonify({'message': 'Detection loop stopped successfully!'})'''

if __name__ == '__main__':
    app.run(debug=True)