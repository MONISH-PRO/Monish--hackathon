import cv2
import numpy as np

def nothing(x):
    pass

# Load image
image = cv2.imread("image.jpg")
image = cv2.resize(image, (640, 480))
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Create a window
cv2.namedWindow("Color Detector")

# Create trackbars for color range
cv2.createTrackbar("LH", "Color Detector", 0, 179, nothing)
cv2.createTrackbar("LS", "Color Detector", 0, 255, nothing)
cv2.createTrackbar("LV", "Color Detector", 0, 255, nothing)

cv2.createTrackbar("UH", "Color Detector", 179, 179, nothing)
cv2.createTrackbar("US", "Color Detector", 255, 255, nothing)
cv2.createTrackbar("UV", "Color Detector", 255, 255, nothing)

while True:
    # Get current positions of trackbars
    lh = cv2.getTrackbarPos("LH", "Color Detector")
    ls = cv2.getTrackbarPos("LS", "Color Detector")
    lv = cv2.getTrackbarPos("LV", "Color Detector")

    uh = cv2.getTrackbarPos("UH", "Color Detector")
    us = cv2.getTrackbarPos("US", "Color Detector")
    uv = cv2.getTrackbarPos("UV", "Color Detector")

    # Create lower and upper HSV range
    lower_bound = np.array([lh, ls, lv])
    upper_bound = np.array([uh, us, uv])

    # Threshold the HSV image
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(image, image, mask=mask)

    # Display result
    cv2.imshow("Original", image)
    cv2.imshow("Mask", mask)
    cv2.imshow("Detected Color", result)

    # Break with ESC key
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
