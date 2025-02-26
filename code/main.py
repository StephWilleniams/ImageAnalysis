import numpy as np
import os
import cv2

file1 = 'cc7_image.png'
img1 = cv2.imread("code/data/" + file1, cv2.IMREAD_GRAYSCALE)

file2 = 'cc7_oralDisc_generous.png'
img2 = cv2.imread("code/data/" + file2, cv2.IMREAD_GRAYSCALE)

file3 = 'cc7_oralDisc_harsh.png'
img3 = cv2.imread("code/data/" + file3, cv2.IMREAD_GRAYSCALE)

file4 = 'cc7_fullOrganism.png'
img4 = cv2.imread("code/data/" + file4, cv2.IMREAD_GRAYSCALE)

images = [img1, img2, img3, img4]

cv2.imshow('image1', img1)
cv2.waitKey(0)
