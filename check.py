import cv2
import numpy as np 

image1 = cv2.imread("1.jpg")
image2 = cv2.imread("3.jpg")

difference = cv2.subtract(image1, image2)

result = not np.any(difference)
print difference
print result

if result is True:
	print "Images are same"

else:
	print "Images are different"