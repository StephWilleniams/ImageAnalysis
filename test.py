import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as nd
#from skimage import data, transform, feature, draw

# Load in the image. Line 1, laptop specific. Line 2, path to CWD. Line 3 path from CWD to data file.
path = "2Month_Exaiptasia_Images/2023.10.16/CC7.290.3_2023.10.16.png"
img = plt.imread(path) # Load specific image

# Convert RGB to grey-scale.

