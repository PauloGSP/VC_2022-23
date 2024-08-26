#import
import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

####################
# Compute Histogram
####################
def compute_histogram(image,histSize, histRange):
	# Compute the histogram
	hist_item = cv2.calcHist([image], [0], None, [histSize], histRange)
	return hist_item

##########################################
# Drawing with openCV
# Create an image to display the histogram
def histogram2image(hist_item, histSize, histImageWidth, histImageHeight, color):

	histImage = np.zeros((histImageWidth, histImageHeight, 1), np.uint8)

	# Width of each histogram bar
	binWidth = int(np.ceil(histImageWidth * 1.0 / histSize))

	# Normalize values to [0, histImageHeight]
	cv2.normalize(hist_item, hist_item, 0, histImageHeight, cv2.NORM_MINMAX)

	# Draw the bars of the nomrmalized histogram
	for i in range(histSize):
		cv2.rectangle(histImage, (i * binWidth, 0), ((i + 1) * binWidth, int(hist_item[i])), color, -1)

	# ATTENTION : Y coordinate upside down
	histImage = np.flipud(histImage)

	return histImage
histsize=250
histrange=[0,256]
histImgWidth=512
histImgHeight=512
color=(125)

img= cv2.imread("TAC_PULMAO.bmp",cv2.IMREAD_UNCHANGED)
height,width=img.shape[0:2]
cv2.namedWindow("Contrast",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Original",img)
#og hist

hist_item=compute_histogram(img,histsize,histrange)
histImg=   histogram2image(hist_item,histsize,histImgWidth,histImgHeight,color)
cv2.imshow("OG histogram",histImg)

EQ = cv2.equalizeHist(img)
cv2.imshow("Histogram EQ",EQ)
#contrast
hist_item=compute_histogram(EQ.astype(np.float32),histsize,histrange)
histImg=   histogram2image(hist_item,histsize,histImgWidth,histImgHeight,color)
cv2.imshow(" histogram eq histogram",histImg)
cv2.waitKey()
cv2.destroyWindow("Display window")