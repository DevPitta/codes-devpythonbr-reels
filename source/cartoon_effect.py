"""
This code uses the opencv library
and results in a cartoon image.

-> Requirements:
    . pip install python-opencv
"""

import cv2

img = cv2.imread('guido.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 1)
edges = cv2.adaptiveThreshold(gray, 255,
                              cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(img, 9, 200, 200)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow('Image', img)
cv2.imshow('Edges', edges)
cv2.imshow('Cartoon', cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
