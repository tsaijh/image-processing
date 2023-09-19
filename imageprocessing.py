# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:32:11 2022

@author: TSAI
"""

import cv2
import numpy as np

# Parameters
blur = 21
canny_low = 50
canny_high = 150
min_area = 0.5
max_area = 0.8
dilate_iter = 10
erode_iter = 10
mask_color = (0.0,0.0,0.0)

path = r'C:\Users\TSAI\Desktop\Chevy 4L60E Two Piece Green Plug No Top Bolt 2WD 2WD BOTTOM.jpg'
#path = r'C:\Users\TSAI\Desktop\human.jpg'
#path = r'C:\Users\TSAI\Desktop\Chevy 4L60E Two Piece Green Plug No Top Bolt 2WD BACK.jpg'
#path = r'C:\Users\TSAI\Desktop\Chevy 4L60E Two Piece Green Plug No Top Bolt 2WD TOP.jpg'

frame = cv2.imread(path)
# Convert image to grayscale        
image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Apply Canny Edge Dection
edges = cv2.Canny(image_gray, canny_low, canny_high)

edges = cv2.dilate(edges, None)
edges = cv2.erode(edges, None)

# get the contours and their areas
contour_info = [(c, cv2.contourArea(c),) for c in cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)[1]]

# Get the area of the image as a comparison
image_area = frame.shape[0] * frame.shape[1]  

# calculate max and min areas in terms of pixels
max_area = max_area * image_area
min_area = min_area * image_area

# Set up mask with a matrix of 0's
mask = np.zeros(edges.shape, dtype = np.uint8)

# Go through and find relevant contours and apply to mask
for contour in contour_info:
    # Instead of worrying about all the smaller contours, if the area is smaller than the min, the loop will break
    if contour[1] > min_area and contour[1] < max_area:
        # Add contour to mask
        mask = cv2.fillConvexPoly(mask, contour[0], (255))

# use dilate, erode, and blur to smooth out the mask
mask = cv2.dilate(mask, None, iterations=dilate_iter)
mask = cv2.erode(mask, None, iterations=erode_iter)
mask = cv2.GaussianBlur(mask, (blur, blur), 0)

# Ensures data types match up
mask = mask.astype('float32') / 255.0           
frame = frame.astype('float32') / 255.0

mask_stack = cv2.merge([mask,mask,mask])

# Blend the image and the mask
masked = (mask_stack * frame) + ((1-mask_stack) * mask_color)
masked = (masked * 255).astype('uint8')
cv2.imwrite(r'C:\Users\TSAI\Desktop\fg.png', masked)