#import
import sys
import numpy as np
import cv2

def printImageFeatures(image):
	# Image characteristics
	if len(image.shape) == 2:
		height, width = image.shape
		nchannels = 1;
	else:
		height, width, nchannels = image.shape

	# print some features
	print("Image Height: %d" % height)
	print("Image Width: %d" % width)
	print("Image channels: %d" % nchannels)
	print("Number of elements : %d" % image.size)

# Read the image from argv
image = cv2.imread( sys.argv[1] , cv2.IMREAD_GRAYSCALE );
#image = cv2.imread( "./lena.jpg", cv2.IMREAD_GRAYSCALE );

if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)

printImageFeatures(image)

cv2.imshow('Orginal', image)

# Gaussian filter 3 x 3
imageGFilter3x3_1 = cv2.GaussianBlur( image, (3,3), 0)
cv2.namedWindow( "Gaussian Filter 3 x 3 - 1 Iter", cv2.WINDOW_AUTOSIZE )
cv2.imshow( "Gaussian Filter 3 x 3 - 1 Iter", imageGFilter3x3_1 )

# Gaussian filter 5 x 5
imageGFilter5x5_1 = cv2.GaussianBlur( image, (5,5), 0)
cv2.namedWindow( "Gaussian Filter 5 x 5 - 1 Iter", cv2.WINDOW_AUTOSIZE )
cv2.imshow( "Gaussian Filter 5 x 5 - 1 Iter", imageGFilter5x5_1 )

# Gaussian filter 7 x 7
imageGFilter7x7_1 = cv2.GaussianBlur( image, (7,7), 0)
cv2.namedWindow( "Gaussian Filter 7 x 7 - 1 Iter", cv2.WINDOW_AUTOSIZE )
cv2.imshow( "Gaussian Filter 7 x 7 - 1 Iter", imageGFilter7x7_1 )

# 2nd time filter 3 x 3
imageGFilter3x3_2 = cv2.GaussianBlur( imageGFilter3x3_1, (3,3), 0)
# 3rd time filter 3 x 3
imageGFilter3x3_3 = cv2.GaussianBlur(  imageGFilter3x3_2, (3,3), 0)
cv2.namedWindow( "Gaussian Filter 3 x 3 - 3 Iter", cv2.WINDOW_AUTOSIZE )
cv2.imshow( "Gaussian Filter 3 x 3 - 3 Iter", imageGFilter3x3_3 )


cv2.waitKey(0)

