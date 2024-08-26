import sys
import numpy as np
import cv2  

image= cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
h,v= image.shape[:2]
mask=np.zeros((h+2,v+2),np.uint8)git