import cv2

img = cv2.imread("Resources/boat.png")
print("img size: ", img.shape)

imgResize = cv2.resize(img, (100, 200))

imgCrop = img[0:300, 300:600, :]

cv2.imshow("org img", img)
cv2.imshow("resize img", imgResize)
cv2.imshow("crop img", imgCrop)

cv2.waitKey(0)
