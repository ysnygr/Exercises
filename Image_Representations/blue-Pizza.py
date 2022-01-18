#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:19:08 2021

@author: yasin
"""


import cv2

img = cv2.imread("/home/yasin/Documents/Desktop/Work/Exercises/Image_Representations/images/pizza_bluescreen.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (110, 100, 100), (130, 255, 255))
inv_mask = cv2.bitwise_not(mask)

pizza = cv2.bitwise_and(img, img, mask=inv_mask)

cv2.imshow("img", img)
cv2.imshow("mask", mask)
cv2.imshow("pizza", pizza)
cv2.waitKey()
cv2.destroyAllWindows()