import numpy as np
import cv2
import sys


def mouse_handler(event,x,y,flags,param):
    global image
    if event == cv2.EVENT_LBUTTONDOWN:
        
        image=cv2.circle(image,(x,y),40,(255,255,255),-1)
        cv2.imshow("Display window",image)
        print("left click")


# Read the image Na verdade isto é o 1.5
image = cv2.imread( sys.argv[1], cv2.IMREAD_UNCHANGED )

if  np.shape(image) == () :
	# Failed Reading
	print("Image file could not be open")
	exit(-1)

newimage= cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
newimage2= cv2.cvtColor(image,cv2.COLOR_RGB2XYZ)
newimage3= cv2.cvtColor(image,cv2.COLOR_RGB2HLS)
newimage4= cv2.cvtColor(image,cv2.COLOR_RGB2HSV)

compact=np.concatenate((newimage2,newimage3,newimage4),axis=1)


# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )
cv2.namedWindow("win",cv2.WINDOW_AUTOSIZE)

cv2.setMouseCallback('Display window',mouse_handler)
# Show the image
cv2.imshow( "Display window", image )
cv2.imshow("win",compact)
# Wait
cv2.waitKey( 0 )

# Destroy the window -- might be omitted
cv2.destroyWindow( "Display window" )
cv2.destroyWindow( "win" )
