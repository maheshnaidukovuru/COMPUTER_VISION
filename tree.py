import cv2 
import numpy as np
kernel=np.ones((10,10),np.uint8)
print(kernel)
path="C:/Users/91628/OneDrive/Pictures/tree.jpeg"
img=cv2.imread(path)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale",imgGray)
cv2.waitKey(0)
