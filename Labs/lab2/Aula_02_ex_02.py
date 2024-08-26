import numpy as np
import cv2
import sys

# Read the image from argv
img = cv2.imread( sys.argv[1] , cv2.IMREAD_UNCHANGED );

if  np.shape(img) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)

GRID_SIZE = 20
print(img.shape)
color=(255,255,255)

try:
	height, width= img.shape
	color=(255,255,255)
except:
	height, width,channel= img.shape

	color=(192,192,192)

for x in range(0, width -1, GRID_SIZE):
    cv2.line(img, (x, 0), (x, height), color, 1, 1)


for x in range(0, height -1, GRID_SIZE):
	cv2.line(img, (0, x), (width, x), color, 1, 1)

cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )

# Show the image
cv2.imshow( "Display window", img )

# Wait
cv2.waitKey( 0 )
cv2.imwrite("grid.png", img)
# Destroy the window -- might be omitted
cv2.destroyWindow( "Display window" )
