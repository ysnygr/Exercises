#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 20:20:21 2021

@author: yasin
"""

import cv2
import numpy as np

color = cv2.imread("/home/yasin/Documents/Desktop/Work/Exercises/Image_Representations/images/water_balloons.jpg")


hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v),axis=1)






cv2.imshow("color",color)
color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
lower_red = np.array([160,00,0]) #example value
upper_red = np.array([210,255,255]) #example value



mask = cv2.inRange(color, lower_red, upper_red)
color_result = cv2.bitwise_and(color, color, mask=mask)
color_result = cv2.cvtColor(color_result, cv2.COLOR_HSV2BGR)



cv2.imshow("Split HSV",hsv_split)
cv2.imshow("result",color_result)
cv2.imwrite("baloon.png",color_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
