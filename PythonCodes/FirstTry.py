# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

#image mainpulation
img = cv2.imread("download.jpg", 1)  #reading image
print(img)#printing its Array form
resized = cv2.resize(img, (int(img.shape[1]*2), int(img.shape[0]*2)))  #resizing

cv2.imshow("Python", resized)  #displaing image

cv2.waitKey(0)
cv2.destroyAllWindows()

#Converting to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Edge Detection
edge = cv2.Canny(gray, 80, 255)   #Based on Canny's Algorithm
cv2.imshow("Outline", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()




