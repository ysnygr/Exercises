#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:19:08 2021

@author: yasin
"""
from PIL import Image, ImageDraw, ImageFilter
import cv2


img = cv2.imread("/home/yasin/Documents/Desktop/Work/Exercises/Image_Representations/images/pizza_bluescreen.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (110, 100, 100), (130, 255, 255))


# inv_mask = cv2.bitwise_not(mask)
# pizza = cv2.bitwise_and(img, img, mask=inv_mask)



img[mask != 0] = [0, 0, 0]
cv2.imshow("img", img)


# cv2.imshow("mask", mask)
# cv2.imshow("pizza", pizza)

cv2.waitKey(0)
cv2.destroyAllWindows() 


# src = pizza    # This code deletes black background of an image.
# tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
# b, g, r = cv2.split(src)
# rgba = [b,g,r,alpha]
# dst = cv2.merge(rgba,4)
# cv2.imwrite("test.png", dst)





background = Image.open("/home/yasin/Documents/Desktop/Work/Exercises/Image_Representations/images/space_background.jpg")
  
foreground = Image.open('/home/yasin/Documents/Desktop/Work/Exercises/Image_Representations/test.png')

background.paste(foreground, (422,409), foreground)

