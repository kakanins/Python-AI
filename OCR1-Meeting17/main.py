from tensorflow.keras.models import load_model
from imutils.contours import sort_contours
import numpy as np
import imutils
import cv2

print("Load the model ....")
model = load_model("handwriting.model")

image = cv2.imread("images/2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edged = cv2.Canny(blurred, 30, 150) #a
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts) 
cnts = sort_contours(cnts, method="left-to-right")[0] #b

print(cnts)

chars = []
for c in cnts: #a
    (x, y, w, h) = cv2.boundingRect(c) #b
    if (w >= 5 and w <= 150) and (h >= 15 and h <= 120): #c
        roi = gray[y:y + h, x:x + w] #d
        thresh = cv2.threshold(roi, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] #e
        (tH, tW) = thresh.shape
        if tW > tH: #f
            thresh = imutils.resize(thresh, width=32)
        else:
            thresh = imutils.resize(thresh, height=32)
        (tH, tW) = thresh.shape
        dX = int(max(0, 32 - tW) / 2.0)
        dY = int(max(0, 32 - tH) / 2.0)
        padded = cv2.copyMakeBorder(thresh, top=dY, bottom=dY, left=dX, right=dX, borderType=cv2.BORDER_CONSTANT, value=(0, 0, 0))
        padded = cv2.resize(padded, (32, 32))
        padded = padded.astype("float32") / 255.0 #a
        padded = np.expand_dims(padded, axis=-1) #b
        chars.append((padded, (x, y, w, h))) #c

boxes = [b[1] for b in chars] #boundingBox coordinate from each character
chars = np.array([c[0] for c in chars], dtype="float32")

preds = model.predict(chars) # Used to identify character based on PreTrained model that has been loaded before
labelNames = "0123456789"
labelNames += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
labelNames = [l for l in labelNames] # Change the above string label compilations into List

for (pred, (x, y, w, h)) in zip(preds, boxes): #a
    i = np.argmax(pred) #b
    prob = pred[i] #c
    label = labelNames[i]
    print("[INFO] {} - {:.2f}%".format(label, prob * 100)) #d
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, label, (x - 10, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

cv2.imshow("Image", image)
cv2.waitKey(0)