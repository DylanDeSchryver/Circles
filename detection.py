import cv2
import numpy as np


def detect_circles(path, min_radius, max_radius, param1, param2):
    # Load image
    img = cv2.imread(path, cv2.IMREAD_COLOR)

    # Resize  image because it is zooming in
    scale_percent = 50  # Adjust this percentage as needed
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to help with edge detection
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    # Use hough circles to detect circles in the image
    circles = cv2.HoughCircles(
        blurred,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=10,
        param1=param1,
        param2=param2,
        minRadius=min_radius,
        maxRadius=max_radius
    )
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # outer circle
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)

            # center of the circle
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

        # show circles
        cv2.imshow('Circles', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("no cricles")
