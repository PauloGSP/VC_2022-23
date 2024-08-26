 # Aula_01_ex_01.py
 #
 # Example of visualization of an image with openCV
 #
 # Paulo Dias - 09/2021



#import
from copy import copy
import numpy as np
import cv2
import sys

# Read the image
image = cv2.imread( sys.argv[1], cv2.IMREAD_UNCHANGED );


if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open")
	exit(-1)

# Image characteristics
height, width = image.shape

print("Image Size: (%d,%d)" % (height, width))
print("Image Type: %s" % (image.dtype))
image_copy=copy(image)

for i in range(0,len(image_copy)):
	for j in range(0,len(image_copy[i])):
		if image_copy[i][j]<128:
			image_copy[i][j]=0 

imgs=np.concatenate((image,image_copy),axis=1)
# Create a vsiualization window (optional)
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )

# Show the image
cv2.imshow( "Display window", imgs )

# Wait
cv2.waitKey( 0 );

# Destroy the window -- might be omitted
cv2.destroyWindow( "Display window" )
