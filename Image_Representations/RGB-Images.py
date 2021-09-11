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


rgb_image = cv2.imread("/home/yasin/Documents/Desktop/Work/Exercises/Image_Representations/images/wa_state_highway.jpg")



rgb_image = np.array(rgb_image)
figure, plots = plt.subplots(ncols=3, nrows=1)
for i, subplot in zip(range(3), plots):
    temp = np.zeros(rgb_image.shape, dtype='uint8')
    temp[:,:,i] = rgb_image[:,:,i]
    subplot.imshow(temp)
    subplot.set_axis_off()
plt.show()
