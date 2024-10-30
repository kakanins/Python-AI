import cv2
from tracker import EuclideanDistTracker
tracker = EuclideanDistTracker()

cap = cv2.VideoCapture("highway.mp4")
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40) #1

while True:
    ret, frame = cap.read()
    roi = frame[340:720, 500:800] #Width dimensions from 500 - 800 & Height dimensions from 340 - 720
    mask = object_detector.apply(roi) #2
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#a
    detections = [] # add this line
    for cnt in contours: #b
        area = cv2.contourArea(cnt)
        if area > 100:                                       #c
            #cv2.drawContours(frame, [cnt], -1,(0,255,0), 2 ) #c
            x, y, w,h = cv2.boundingRect(cnt)
            detections.append([x,y,w,h]) # add this line
            #cv2.rectangle(roi, (x,y), (x+w, y+h), (0,255,0), 2)
            #print(detections)  # add this line
            boxes_ids = tracker.update(detections)
            for boxes_id in boxes_ids:
                x,y,w,h,id = boxes_id
                cv2.putText(roi, str(id), (x,y -15), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2 )
                cv2.rectangle(roi, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow("Roi", roi)
    cv2.imshow("mask", mask) #2
    key = cv2.waitKey(30)
    if key==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()