import cv2
print(cv2.__version__)
imagepath=input("Drag and drop the Image ->")
print(imagepath)
image = cv2.imread(imagepath)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert=cv2.bitwise_not(gray_image)
blur=cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)

pencil_sketch = cv2.divide(gray_image, invertedblur,scale=225.0)
cv2.imwrite("output.png",pencil_sketch)
cv2.imshow("original image", image)
#cv2.waitKey()
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey()