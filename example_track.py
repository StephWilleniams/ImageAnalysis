# Aiptasia identification code
# Author: Stephen Williams
# Date of origin: 01/29/2024

# NOTE: currently contains memory problems, this can cause segmentation fault errors.
# Keep running the code and it seems to eventually run properly.

# Public inclusions
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as nd
from skimage import transform, feature, draw

# Load in the image.
# Note: Here we have three cases to test. Details given in line comments.
#path = "2Month_Exaiptasia_Images/2023.10.16/CC7.290.3_2023.10.16.png" # Manual value optimised example.
path = "2Month_Exaiptasia_Images/2023.10.20/CC7.290.3_2023.10.20.png" # Non-value optimised example (based on prev).
#path = "2Month_Exaiptasia_Images/2023.10.20/H2.340.3_2023.10.20.png" # Non-value optimised, different strain (based on first).
img = plt.imread(path) # Load desired image.

# Convert RGB to grey-scale (inefficient).
img_GS = np.zeros([np.size(img[:,1,0]),np.size(img[1,:,0])])
img_GS = 1-(np.sqrt(np.square(img[:,:,0])+np.square(img[:,:,1])+np.square(img[:,:,2]))/np.sqrt(3))

# Crop the image.
# Select the coordinates that put the boundaries at the edge of the printed image.
# HINT: Use optional comment labellel (OPT1) to figure this out.
x1=380; x2=1680 # Note argument 2 of img is the horizontal (here labelled x).
y1=40; y2=1040 # Note argument 1 of img is the vertical (here labelled y).

# OPT1 - plotting helper to determine crop.
# plt.imshow(img_GS[y1:y2,x1:x2])
# plt.show()

# Image processing.
img_GS_inv = 1-img_GS[y1:y2,x1:x2] # Convert from brightfield to darkfield.
img_GS_inv = nd.gaussian_filter(img_GS_inv,0) # Optional Gaussian filter, currently off.
thresh = 0.4 # Threshold to convert the image to a binary.
img_bin = np.zeros([ np.size(img_GS_inv,0),np.size(img_GS_inv,1)]) # Preallocate a store for the binary image.
# Loop through elements in image to determine if they're above/below threshold.
for row_ind,row in enumerate(img_GS_inv):
    for col_ind,element in enumerate(row):
        if (element > thresh): 
            img_bin[row_ind,col_ind] = 0
        else: 
            img_bin[row_ind,col_ind] = 1; # img_GS_inv[row_ind,col_ind] # Uncomment here to stop upper bound thresholding.

# Edge detection.
#edges = feature.canny(img_bin, sigma=2.5, low_threshold=0.3, high_threshold=0.8) # Low noise filter, high thresholds.
edges = feature.canny(img_bin, sigma=5, low_threshold=0.075, high_threshold=0.3) # High noise filter, low thresholds.
            
# Hough circle detection.
hough_radii = np.arange(7, 21, 1)  # Circle radii to attempt to locate (min,max,incr.)
hough_res = transform.hough_circle(edges, hough_radii) # I'm not sure what this does.
thresh2 = 0.45 # Circle peak intensity threshold.
accums, cx, cy, radii = transform.hough_circle_peaks(hough_res, hough_radii, 15, 15, thresh2*np.max(hough_res) )  # Get the detected set of circles.

# Draw detected circles
fig, ax = plt.subplots(); ax.imshow(img_GS_inv) # Set up a background figure

# Plot each of the circles
for center_y, center_x, radius in zip(cy, cx, radii):
    circ = plt.Circle((center_x, center_y), radius, color='red', linewidth=2, fill=False)
    ax.add_patch(circ)

# Show the current plot (not needed for IDE with internal plotting).
plt.axis('off'); plt.show()
