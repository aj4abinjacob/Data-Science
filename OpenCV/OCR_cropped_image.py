#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 08:44:41 2021

@author: christy
"""


import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('data/cards/ronaldo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#base_coor = [48, 2, 327, 31]

default_shape = (593, 447, 3)

base_coor =  [50, 310, 400, 375] #x1,y1,x2,y2

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    #print(b[0])
    ix=int(b[1])
    iy=h-int(b[2])
    x = int(b[3])
    y = h-int(b[4])
    img = cv2.rectangle(img, (ix, iy), (x,y), (0, 255, 0), 2)


img= img[base_coor[1]:base_coor[3],base_coor[0]:base_coor[2]]

text  = pytesseract.image_to_string(img)
print(text)


import matplotlib.pyplot as plt

plt.imshow(img)
plt.title("Bounding Boxes With Dictionary")
plt.show()
