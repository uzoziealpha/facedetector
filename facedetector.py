import cv2

#cascade classifier
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("photo1.jpg")

#grey scale images are better for a face search
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#search cascade classifier to return coordinates
#of the pixels Widht, height

faces=face_cascade.detectMultiScale(gray_img,
#you can change the numbers to get different scales
scaleFactor=1.05,
minNeighbors=5)

#for loop to create a rectangular layer
for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y),(x+w,+y+h), (0,255,0),3)


print(type(faces))
print(faces)


cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()