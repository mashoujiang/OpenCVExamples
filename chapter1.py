import cv2

"""
install opencv:
 python3 -m pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple --user

capture video camera with specific resolution
"""

cap = cv2.VideoCapture(0)  # 0 is default device
cap.set(3, 640)  # 3 means width which has to be set with support resolution
cap.set(4, 480)  # 4 means height which has to be set with support resolution
cap.set(10, 100)  # 10 means brightness which set to 100

while True:
    success, img = cap.read()
    imgCanny = cv2.Canny(img, 100, 200)
    cv2.imshow("Video", imgCanny)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press 'q' to exit
        break
