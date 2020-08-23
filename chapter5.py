import cv2
import numpy as np

img = cv2.imread("Resources/boat.png")

width, height = 250, 350
pts1 = np.float32(([111, 222], [333, 222], [150, 480], [400, 455]))
pts2 = np.float32(([0, 0], [width, 0], [0, height], [width, height]))

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Out img", imgOutput)
cv2.waitKey(0)
