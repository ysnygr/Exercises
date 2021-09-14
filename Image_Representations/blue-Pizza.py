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



image = cv2.imread("/home/yasin/Documents/Desktop/Work/Exercises/Image_Representations/images/pizza_bluescreen.jpg")
print("image dimensions: ", image.shape)
print(image.dtype)


rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

plt.imshow(rgb_image)

rgb_image[:,:,2] = np.zeros([rgb_image.shape[0], rgb_image.shape[1]])


plt.imshow(rgb_image)
