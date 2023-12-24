
import cv2
import numpy as np

# Load the image
bw = cv2.imread('C:/Users/khina/OneDrive/Desktop/Do_an/Vi_nhua/Data_vinhua/Device_mask_img/Mask/25.png',0)

# Display the binary image
cv2.imshow("Binary Image", bw)

# Perform the distance transform algorithm
dist = cv2.distanceTransform(bw, cv2.DIST_L2, 5)

# Normalize the distance transform image
cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)

# Display the distance transform image
cv2.imshow("Distance Transform Image", dist)

# Threshold to obtain the peaks (markers for foreground objects)
_, dist = cv2.threshold(dist, 0.8, 1.0, cv2.THRESH_BINARY)

# Create a kernel for dilation
kernel1 = np.ones((3, 3), np.uint8)

# Dilate the dist image
dist = cv2.dilate(dist, kernel1)

# Display the peaks (markers)
cv2.imshow("Peaks", dist)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()