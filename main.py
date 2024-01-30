
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as nd
import os

# File path of the data.
path = "Kaden_pilot/2Month_Exaiptasia_Images/"
dir_list = [] 

# Create a list of all the directories containing data
for ents in os.listdir(path):
    if ents.startswith('.DS') == False : dir_list.append(ents)
    
# Add in some code which systematically runs though the directories for a specific experiment/set
#for dir in dir_list:
#    pass

# Load in the images
ind1 = 7;
#ind2 = 5;
date_string1 = dir_list[ind1]
#date_string2 = dir_list[ind2]
pathtemp1 = "Kaden_pilot/2Month_Exaiptasia_Images/" + date_string1 + "/CC7.340.1_" + date_string1 +  ".png"
#pathtemp2 = "Kaden_pilot/2Month_Exaiptasia_Images/" + date_string2 +  "/CC7.340.1_" + date_string2 + ".png"
img1 = plt.imread(pathtemp1)
#img2 = plt.imread(pathtemp2)

# Convert RGB to gray-scale
GS_img1 = 1 - (np.sqrt(np.square(img1[:,:,0]) + np.square(img1[:,:,1]) + np.square(img1[:,:,2]))/np.sqrt(3))
#GS_img2 = 1 - (np.sqrt(np.square(img2[:,:,0]) + np.square(img2[:,:,1]) + np.square(img2[:,:,2]))/np.sqrt(3))

# Crop the image in some systematic way, suggestion for a possible way to do this below.
#GS_img1_GF = nd.gaussian_filter(GS_img1,6) # Alternative smoothing method
test_line_x = np.mean(GS_img1[:,:],1)
test_line_y = np.mean(GS_img1[:,:],0)

#  Locally smooth data by averaging over a window centered on the data-point
hw = 20
for points,inds in enumerate(test_line_x):
    if inds > hw and inds < len(test_line_x)-hw :
        test_line_x = np.mean(test_line_x[inds-hw:inds+hw])
        
for points,inds in enumerate(test_line_y):
    if inds > hw and inds < len(test_line_y)-hw :
        test_line_y = np.mean(test_line_y[inds-hw:inds+hw])

threshx = 1
threshy = 1

test_line_x[ test_line_x > np.max(test_line_x)*threshx ] = np.max(test_line_x)*threshx
test_line_y[ test_line_y > np.max(test_line_y)*threshy ] = np.max(test_line_y)*threshy
padding = 50

max_x_R = np.max(test_line_x[1+int(len(test_line_x)/2):-1])
np.arg
index_x_R = int(  )

ndex_x_L = np.argmax(test_line_x[0:int(len(test_line_x)/2)]) + padding

index_y_T = int(len(test_line_y)/2) + np.argmax(test_line_y[1+int(len(test_line_y)/2):-1]) - padding

index_y_B = np.argmax(test_line_y[0:int(len(test_line_y)/2)]) + padding
GS_img1_slice = GS_img1[index_x_L:index_x_R,index_y_B:index_y_T]

# plotting tools
plt.imshow(GS_img1_slice)
#plt.plot(test_line_y)

## end

