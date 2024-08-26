import sys
import numpy as np
import cv2

# Read the image from argv
image = cv2.imread( "lena.jpg" , cv2.IMREAD_GRAYSCALE )

# flood fill
image2 = image.copy()
h, w = image.shape[:2]
mask = np.zeros((h + 2, w + 2), np.uint8)
_, image_flo, mask, _ = cv2.floodFill(image, mask, (430,30), 0, loDiff=5, upDiff=5)

cv2.imshow('Orginal', image2)
cv2.imshow('Flood FIlled Image', image_flo)

cv2.waitKey(0)