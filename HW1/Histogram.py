import numpy as np
import cv2
from matplotlib import pyplot as plt

img_1 = np.zeros((400,400),np.uint8) #  img_1 is the image on the left side.
img_2 = np.zeros((400,400),np.uint8) #  img_2 is the image on the right side.

#아이디어 8x8 
#  0 1  2  3  4  5  6  7  열 
#0짝 홀 짝 홀 짝 홀 짝  홀
#1홀 짝 홀 짝 홀 짝 홀  짝  짝에서 색칠하기 시작지점 (행*50,열*50) 끝지점(행*50,짝*100) 
#2행
#3
#4
#5
#6
#7
cv2.rectangle(img_1,(0,0),(200,400),(255),-1) # creating the image_1 via painting half into white (255)

for x in range(0,8 * 50):                          
    for y in range(0,8 * 50):
        if((x//50+y//50)%2==0):
            img_2[y, x] = 255
# for x in range(0,8):
#     for y in range(0,8):
#         if((x+y)%2==0):
#             img_2[y, x] = 255
            # cv2.rectangle(img_2, (50 * x, 50 * y), (50 * (x+1) - 1 , 50 * (y+1) - 1),(255), -1) #홀수행 (50,50) (50,150) , (50,250) , (50,350) 에서 점찍음

cv2.imshow('img_2',img_2)

plt.hist(img_1.ravel(),255,[0,255])
plt.hist(img_2.ravel(),255,[0,255])

plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()