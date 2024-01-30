
# Public inclusions
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as nd
from skimage import transform, feature, draw

# Load in the image. Line 1, laptop specific. Line 2, path to CWD. Line 3 path from CWD to data file.

# Note: Here 

#path = "2Month_Exaiptasia_Images/2023.10.16/CC7.290.3_2023.10.16.png" # Value optimised example
#path = "2Month_Exaiptasia_Images/2023.10.20/CC7.290.3_2023.10.20.png" # Non-value optimised example
path = "2Month_Exaiptasia_Images/2023.10.20/H2.340.3_2023.10.20.png" # Non-value optimised, different strain
img = plt.imread(path) # Load specific image

# Convert RGB to grey-scale.
img_GS = np.zeros([np.size(img[:,1,0]),np.size(img[1,:,0])])
img_GS = 1-(np.sqrt(np.square(img[:,:,0])+np.square(img[:,:,1])+np.square(img[:,:,2]))/np.sqrt(3))

# Select the coordinates that put the boundaries at the edge of the printed image
# Use optional comment labellel (OPT1) to figure this out.
# Note argument 1 is the vertical (here labelled y).
# Note argument 2 is the horizontal (here labelled x).
x1=380; x2=1680; y1=40; y2=1040; 

img_GS_inv = 1-img_GS[y1:y2,x1:x2]
img_GS_inv = nd.gaussian_filter(img_GS_inv,0)
thresh = 0.4
img_bin = np.zeros([ np.size(img_GS_inv,0),np.size(img_GS_inv,1)])
for row_ind,row in enumerate(img_GS_inv):
    for col_ind,element in enumerate(row):
        if (element > thresh): 
            img_bin[row_ind,col_ind] = 0
        else: 
            img_bin[row_ind,col_ind] = 1;#img_GS_inv[row_ind,col_ind]
            
# plt.imshow(img_bin)
# plt.show()

# Edge detection (optional)
#edges = feature.canny(img_bin, sigma=2.5, low_threshold=0.3, high_threshold=0.8)
edges = feature.canny(img_bin, sigma=5, low_threshold=0.075, high_threshold=0.3)
            
# Hough circle detection
hough_radii = np.arange(7, 21, 1)  # Adjust radius range as needed
hough_res = transform.hough_circle(edges, hough_radii)
accums, cx, cy, radii = transform.hough_circle_peaks(hough_res, hough_radii, 15, 15, 0.45*np.max(hough_res) )  # Adjust number of peaks

# # Draw detected circles
fig, ax = plt.subplots()
ax.imshow(img_GS_inv)

for center_y, center_x, radius in zip(cy, cx, radii):
    circ = plt.Circle((center_x, center_y), radius, color='red', linewidth=2, fill=False)
    ax.add_patch(circ)

plt.axis('off')
plt.show()
