#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 14:16:56 2021

@author: yasin
"""

import cv2
import glob
from os import path



def load_dataset(path_folder):
   
    image_list = []
    f_list = ["day","night"]
    for folder_name  in f_list:
        folder = path.join(path_folder , folder_name, "*.jpg") 
        for img in glob.glob(folder):           
            img_read = cv2.imread(img,cv2.IMREAD_UNCHANGED)
            image_list.append((img_read , folder_name ))
            
    return image_list

traning_dir ="/home/yasin/Documents/Desktop/Work/Exercises/Image_Representations/day_night_images/training/"

img_lst = load_dataset(traning_dir)


def resize(img, width, height):    
    
    dim = (width, height)
    img_resize =  cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    return img_resize



def numeric(label):
    if label =="day":
        value = 1
    else:
        value = 0
    return value
 
    

    
def standardize(img_list):
    img_standart_list = []
    for img in img_list:
        img_resized = resize(img[0],1100,600)
        img_label = numeric(img[1])
        img_standart_list.append((img_resized, img_label))
        
    return img_standart_list   
        
standart_list = standardize(img_lst)        

        
print(standart_list[185])  
    
    
    