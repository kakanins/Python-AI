import numpy as np
import cv2 

# Import library Numpy and OpenCV 
min_confidence = 0.5  # Minimum confidence model value when detecting faces. Minimum 50% of the objects are faces
net = cv2.dnn.readNetFromCaffe("models/deploy.prototxt.txt", "models/res10_300x300_ssd_iter_140000.caffemodel")
image = cv2.imread('images/masked.jpg')  # Load the image that will later detect the face

# Access the image size
height, width = image.shape[0], image.shape[1]

# Create a blob from the image
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 117.0, 123.0))

# Set the input to the network
net.setInput(blob)

# Forward pass to get detections
detections = net.forward()

# Loop through the detections
for i in range(0, detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > min_confidence:
        # Get the bounding box coordinates
        box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
        (startX, startY, endX, endY) = box.astype('int')

        # Draw a red rectangle around the face
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)

        # Display the confidence as text below the rectangle
        text = f"{confidence * 100:.2f}%"
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

# Display the final image with rectangles and text
cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
