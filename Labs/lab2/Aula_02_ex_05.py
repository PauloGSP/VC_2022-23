
#import
import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Read the image from argv
image = cv2.imread( sys.argv[1] , cv2.IMREAD_UNCHANGED )

if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)
height, width, channels = None, None, None
# Image characteristics
if len (image.shape) > 2:
    image = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY )
    print ("The loaded image is NOT a GRAY-LEVEL image !")

height, width = image.shape



# Display the image
cv2.namedWindow("Original Image")
cv2.imshow("Original Image", image)

# print some features
nchannels = 1
print("Image Size: (%d,%d)" % (height, width))
print("Image Type: %d" % nchannels)
print("Number of elements : %d" % image.size)

print("Image Size: (%d,%d)" % (height, width))

# Size
histSize = 256	 # from 0 to 255
# Intensity Range
histRange = [0, 256]

stretched = image.copy()

min_val,max_val, _, _=cv2.minMaxLoc(stretched)

for i in range(0, len(stretched)):
    for j in range(0, len(stretched[i])):
        stretched[i][j] = (stretched[i][j] - min_val) * 255 / (max_val - min_val)

cv2.namedWindow("Contrast-Stretching Image")
cv2.imshow("Contrast-Stretching Image", stretched)

# Compute the histogram
hist_item = cv2.calcHist([image], [0], None, [histSize], histRange)

##########################################
# Drawing with openCV
# Create an image to display the histogram
histImageWidth = 512
histImageHeight = 512
color = (125)
histImage = np.zeros((histImageWidth,histImageHeight,1), np.uint8)

# Width of each histogram bar
binWidth = int (np.ceil(histImageWidth*1.0 / histSize))

# Normalize values to [0, histImageHeight]
cv2.normalize(hist_item, hist_item, 0, histImageHeight, cv2.NORM_MINMAX)

# Draw the bars of the nomrmalized histogram
for i in range (histSize):
	cv2.rectangle(histImage,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item[i]) ), (125), -1)

# ATTENTION : Y coordinate upside down
histImage = np.flipud(histImage)


# Compute the histogram
hist_item = cv2.calcHist([stretched], [0], None, [histSize], histRange)

##########################################
# Drawing with openCV
# Create an image to display the histogram
histStretchedWidth = 512
histStretchedHeight = 512
color = (125)
histStretched = np.zeros((histStretchedWidth,histStretchedHeight,1), np.uint8)

# Width of each histogram bar
binWidth = int (np.ceil(histStretchedWidth*1.0 / histSize))

# Normalize values to [0, histStretchedHeight]
cv2.normalize(hist_item, hist_item, 0, histStretchedHeight, cv2.NORM_MINMAX)

# Draw the bars of the nomrmalized histogram
for i in range (histSize):
	cv2.rectangle(histStretched,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item[i]) ), (125), -1)

# ATTENTION : Y coordinate upside down
histStretched = np.flipud(histStretched)

cv2.imshow('Original Histogram', histImage)
cv2.imshow('Contrast-Stretching Histogram', histStretched)
cv2.waitKey(0)

##########################
# Drawing using matplotlib
plt.plot(hist_item,'r')
plt.xlim(histRange)
plt.show()



