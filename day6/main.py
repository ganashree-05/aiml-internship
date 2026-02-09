import cv2
import numpy as np

with open("image.jpg", "rb") as f:
    image = f.read()

# Convert bytes to numpy array
img_array = np.frombuffer(image, np.uint8)

# Decode image
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

# Show image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
