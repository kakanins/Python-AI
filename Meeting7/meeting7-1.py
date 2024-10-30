import cv2  # dijelaskan di bagian a
import numpy as np

img = cv2.imread("Meeting7/avenger.jpg")
img = cv2.resize(img, (300, 400))
mask = np.zeros(img.shape[:2], dtype="uint8")# explained in section (a)
cv2.circle(mask, (160,200), 165, 255, -1) # explained in section (b)
img = cv2.bitwise_and(img, img, mask = mask) # explained in section (c)
red = (255,255,255)
#img = cv2.putText(img, "OpenCV", (100, height-30), cv2.FONT_HERSHEY_COMPLEX, 1 , red, 2)
cv2.imshow("Mask", mask)
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows() # explained in section d