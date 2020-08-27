import cv2
import numpy as np

"""
install opencv:
 python3 -m pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple --user

capture video camera with specific resolution
"""

cap = cv2.VideoCapture(0)  # 0 is default device
cap.set(3, 640)  # 3 means width which has to be set with support resolution
cap.set(4, 480)  # 4 means height which has to be set with support resolution
cap.set(10, 150)  # 10 means brightness which set to 100

myColors = [[169, 177, 0, 179, 255, 255]]
myColorValues = [[0, 97, 255]]
myPoints = []


def findColor(img, colors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = []
    for color, color_value in zip(colors, myColorValues):
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        if x and y:
            newPoints.append([x, y, color_value])

        # cv2.circle(imgResult, (x, y), 10, color_value, cv2.FILLED)
        # cv2.imshow("Image", mask)
    return newPoints


def drawOnCanvas(points):
    for point in points:
        cv2.circle(imgResult, (point[0], point[1]), 10, point[2], cv2.FILLED)


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors)
    if len(newPoints):
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints):
        drawOnCanvas(myPoints)

    cv2.imshow("Video", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press 'q' to exit
        break
