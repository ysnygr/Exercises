#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 14:16:56 2021

@author: yasin
"""
import numpy as np
import cv2
import glob
from os import path



def load_dataset(path_folder):
   
    image_list = []
    f_list = ["day","night"]
    for folder_name  in f_list:
        folder = path.join(path_folder, folder_name, "*.jpg") 
        for img in glob.glob(folder):           
            img_read = cv2.imread(img)
            image_list.append((img_read, folder_name))
            
    return image_list


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
    
       
def Volume_Avg(vol_2d):   
    vol = vol_2d[:,:,2]        
    average_vol = np.mean(vol)
    return average_vol



def Volume_Assort(img):
    img_avg = Volume_Avg(img)
    if img_avg >90:
        value = 1
    else:
        value = 0
    return value


def verify(lst):
    verify_lst = []
    for img in lst:
        img_assort = Volume_Assort(img[0])
        if img_assort == img[1]:
            pass
        else:
            verify_lst.append((img[0], img[1], img_assort))
    return verify_lst


test_dir ="/home/yasin/Documents/Desktop/Work/Exercises/Image_Representations/day_night_images/test/"
img_lst = load_dataset(test_dir)
standart_list = standardize(img_lst)  
verify_list = verify(standart_list)
accuracy = 1- (len(verify_list) / len(standart_list))
print(accuracy)