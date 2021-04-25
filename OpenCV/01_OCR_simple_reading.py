# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:15:26 2020

@author: chris
"""
#download tesseract - https://github.com/UB-Mannheim/tesseract/wiki - for windows
#https://tesseract-ocr.github.io/tessdoc/Installation.html -for linux
#install pytesseract - pip install pytesseract

import time

import cv2
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Reading the image using CV
img = cv2.imread('data/testocr.png') 
start = time.time()
print("Text extracted using Tesseract\n")
#Extracting the text from image
text = pytesseract.image_to_string(img)
print(text)
end = time.time()
t = round(end-start,2)
print("\nTime Taken   ", t, " (s)")