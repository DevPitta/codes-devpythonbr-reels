"""
This code uses the opencv-python library
and mediapipe and results in the detection of faces in an image.

-> Requirements
    . pip install opencv-python
    . pip install mediapipe
"""

import cv2
import mediapipe as mp

drawing = mp.solutions.drawing_utils
face = mp.solutions.face_detection.FaceDetection(
    model_selection=1,
    min_detection_confidence=0.5
)

image = cv2.imread('media/bigbang.jpg')
image_input = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
result = face.process(image_input)

if not result.detections:
    print('No face detected!')
else:
    for detection in result.detections:
        drawing.draw_detection(image, detection)

cv2.imwrite('detected_image.jpg', image)
cv2.imshow('image', image)
cv2.waitKey(0)
