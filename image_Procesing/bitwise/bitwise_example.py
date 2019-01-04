import cv2
import numpy as np



img1=cv2.imread("first.png")
img2=cv2.imread("second.png")
bit_and=cv2.bitwise_and(img1,img2)
bit_or=cv2.bitwise_or(img1,img2)
bit_xor=cv2.bitwise_xor(img1,img2)
bit_not_1=cv2.bitwise_not(img1)
bit_not_2=cv2.bitwise_not(img2)


cv2.imshow("image 1",img1)
cv2.imshow("image 2",img2)
cv2.imshow("bit_and",bit_and)
cv2.imshow("bit_or",bit_or)
cv2.imshow("bit_not_1",bit_not_1)
cv2.imshow("bit_not_2",bit_not_2)
cv2.waitKey(0)
cv2.destroyAllWindows()


