import cv2
from PIL import Image, ImageChops

img1 = Image.open('duck.jpg')
img2 = Image.open('duck2.jpg')

diff = ImageChops.difference(img1, img2)

diff.show()

A = cv2.imread('duck.jpg', cv2.IMREAD_UNCHANGED)
B = cv2.imread('duck2.jpg', cv2.IMREAD_UNCHANGED)

#check to make sure the images are the same size
if A.shape[0] != B.shape[0]:
    print("height is not equal between the images")
if A.shape[1] != B.shape[1]:
    print("width is not equal between the images")

height = A.shape[0]
width = A.shape[1]

errorL2 = cv2.norm(A, B, cv2.NORM_L2)
similarity = (1 - (errorL2/(height*width))) * 100
print('Similarity = ',similarity)
