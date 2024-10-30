import numpy as np
import cv2

# Import library Numpy and OpenCV
min_confidence = 0.5  # Minimum confidence model value when detecting faces. Minimum 50% of the objects are faces
net = cv2.dnn.readNetFromCaffe(
    "models/deploy.prototxt.txt", "models/res10_300x300_ssd_iter_140000.caffemodel"
)

# Open a connection to the webcam (assuming it's the default camera, index 0)
cap = cv2.VideoCapture(0)

while True:
    # Capture video frame-by-frame
    ret, frame = cap.read()

    # Access the frame size, namely height and width
    height, width = frame.shape[0], frame.shape[1]

    # Preprocess the frame for face detection
    blob = cv2.dnn.blobFromImage(
        cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 117.0, 123.0)
    )

    # Set the input to the neural network
    net.setInput(blob)

    # Forward pass to get detections
    detections = net.forward()

    # Loop through the detections
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]  # Confidence of the detection
        if confidence > min_confidence:
            # Calculate the bounding box coordinates of the detected face
            box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (startX, startY, endX, endY) = box.astype("int")

            # Draw a red rectangle around the detected face
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)

            # Display the confidence as text below the rectangle
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.putText(
                frame,
                text,
                (startX, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.45,
                (0, 0, 255),
                2,
            )

    # Display the resulting frame
    cv2.imshow("Frame", frame)

    # Break the loop if 'q' key is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
