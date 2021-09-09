#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:19:08 2021

@author: yasin
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2


image = mpimg.imread("/home/yasin/Documents/Desktop/Work/Exercises/Image_Representations/images/waymo_car.jpg")
print("image dimensions: ", image.shape)

gri_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
plt.imshow(gri_image, cmap = "gray")

print("image dimensions: ", gri_image.shape)

x = 50
y = 180

print(gri_image[y,x])

maxValue = np.amax(gri_image)

print("maxValue: ", maxValue)

minValue= np.amin(gri_image)

print("minValue: ", minValue)

argMax = np.argmax(gri_image)
argMin = np.argmin(gri_image)


print("argMax:", argMax)

maxCoordinates = np.unravel_index( argMax , gri_image.shape)

print("maxCoordinates:", maxCoordinates)

minCoordinates = np.unravel_index( argMin , gri_image.shape)

print("minCoordinates:", minCoordinates)

array_2D = np.array([[5, 8, 20, 80, 160],
                     [70, 45, 6, 14, 37],
                     [58, 94, 47, 25, 19],
                     [78, 67, 63, 39, 84],
                     [0, 92, 13, 57, 61]
                     ])
plt.matshow(array_2D, cmap ="gray")









