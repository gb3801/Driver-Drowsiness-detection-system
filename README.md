# Drowsiness Detection System using Facial Landmarks
## Overview
This project implements a Drowsiness Detection System using facial landmarks. 
The system utilizes the dlib library to detect facial landmarks and determines if the person is drowsy based on certain facial features.

## Dependencies
Make sure to install the required dependencies before running the project. 

## You can install them using the following command:
bash
Copy code
''' pip install flask imutils opencv-python dlib pygame '''

## Project Structure

* drowsiness_detection.py: The main script containing the drowsiness detection logic using facial landmarks.
* shape_predictor_68_face_landmarks.dat: A pre-trained model for detecting 68 face landmarks.
* templates: Contains HTML templates for the Flask web application.
* static: Can be used to store static files like CSS or client-side JavaScript.

## How to Run
## Clone the repository:
bash
Copy code
''' git clone https://github.com/your-username/your-repo.git '''
''' cd your-repo '''

## Run the Flask application:
bash
Copy code
''' python drowsiness_detection.py '''
Open your web browser and go to http://127.0.0.1:5000/ to access the application.

## Usage
The application uses your computer's webcam to monitor your face.
Facial landmarks are detected in real-time, and the system checks for signs of drowsiness.
An alert is triggered if drowsiness is detected.
Press 'q' to exit the application.

## Configuration
You can adjust the sensitivity of drowsiness detection by changing the thres variable in the drowsiness_detection.py script.

## Image Output
![Interface](images/Screenshot%20(19).png)

## Disclaimer
This project is for educational and experimental purposes only. 
Do not use it in situations where accurate drowsiness detection is critical for safety.

## Credits
* dlib: A toolkit for machine learning and computer vision.
* Flask: A lightweight WSGI web application framework.
* OpenCV: An open-source computer vision and machine learning software library.
* Pygame: A cross-platform set of Python modules designed for writing video games.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
