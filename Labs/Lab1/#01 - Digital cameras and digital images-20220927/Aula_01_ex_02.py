import numpy as np
import cv2
import sys

# Read the image Na verdade isto é o 1.4
image = cv2.imread( sys.argv[1], cv2.IMREAD_UNCHANGED );
image2 = cv2.imread( sys.argv[2], cv2.IMREAD_UNCHANGED );


if  np.shape(image) == () :
	# Failed Reading
	print("Image file could not be open")
	exit(-1)


dtype = -1;
img3=cv2.subtract(image, image2, dtype)
imgs=np.concatenate((image,image2,img3),axis=1)


# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )

# Show the image
cv2.imshow( "Display window", imgs )

# Wait
cv2.waitKey( 0 );

# Destroy the window -- might be omitted
cv2.destroyWindow( "Display window" )
