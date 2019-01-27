# OpenCV program to perform Edge detection in real time
# import libraries of python OpenCV
# where its functionality resides
import cv2
import time

# np is an alias pointing to numpy library
import numpy as np

# capture frames from a camera
cap = cv2.VideoCapture(0)

# Set framerate
# cap.set(cv2.cv.CV_CAP_PROP_FPS, 1)

img_counter = 0
frame = 0;

# loop runs if capturing has been initialized
while (1):

    # reads frames from a camera
    ret, frame = cap.read()

    # finds edges in the input image image and
    # marks them in the output map edges
    edges = cv2.Canny(frame, 100, 200)

    pixels = cv2.countNonZero(edges)
    print(pixels)

    cv2.imshow('Edges', edges)

    if pixels > 8000:
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, edges)
        img_counter += 1
        # cv2.putText(edges, 'Picture Taken!', (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 4,  (255, 255, 255), 2, cv2.LINE_AA)
        print("Picture taken!")
        time.sleep(5)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    if k % 256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, edges)
        img_counter += 1

    time.sleep(0.5)

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()


# the location of cv2 in my puter, dont worry about it
# /usr/local/Cellar/opencv/4.0.1/lib/python3.7/site-packages/cv2/python-3.7/cv2.cpython-37m-darwin.so