import cv2  # dijelaskan di bagian a

img = cv2.imread("Meeting7/avenger.jpg") # explained in section b
print(img.shape)
img = cv2.resize(img, (300, 400))
img = cv2.resize(img, (0,0), fx=2, fy=2)
#img = cv2.blur(img, (10,10)) #averaging filtering
img = cv2.boxFilter(img, -2, (10, 10)) #averaging filtering
img = cv2.GaussianBlur(img, (15,15), 0) #odd number only for the kernel size
cv2.imshow("Image", img)  # explained in section c

cv2.waitKey(0)
cv2.destroyAllWindows() # explained in section d