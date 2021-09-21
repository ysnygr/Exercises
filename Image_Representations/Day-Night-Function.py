#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:04:07 2021

@author: yasin
"""
import cv2
import glob



Image_list = []
 
   
for x in glob.glob("/home/yasin/Documents/Desktop/Work/Exercises/Image_Representations/day_night_images/training"):
    



    for img in glob.glob("/home/yasin/Documents/Desktop/Work/Exercises/Image_Representations/day_night_images/training/day/*.jpg"):
            
        img_read = cv2.imread(img)
        
        img_shape = img_read.shape
         
        img_index = ','.join (str(v) for v in img_shape)
        
        img_tuple = (img_index,)
        
        day = ("day",)
        
        
        
        Image_list.append(img_tuple + day)
        
       
    
    for img in glob.glob("/home/yasin/Documents/Desktop/Work/Exercises/Image_Representations/day_night_images/training/night/*.jpg"):
            
        img_read = cv2.imread(img)
        
        img_shape = img_read.shape
         
        img_index = ','.join (str(v) for v in img_shape)
        
        img_tuple = (img_index,)
        
        night = ("night",)
        
        
        
        Image_list.append(img_tuple + night)


