import numpy as np
import cv2
import matplotlib.pyplot as plt

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

def get_histogram(img, bins = 100):#100개 구간으로 슬라이싱한 히스토그램 데이터입니다., density=True
    min_data = np.min(img)
    max_data = np.max(img)

    dx = (max_data - min_data) / bins #bins가 한번 돌아갈때마다 x축을 그리는 구간이 dx입니다.
    x = np.zeros(bins)
    y = np.zeros(bins+1)#for문이 0~bin까지 돌기 때문에 y 배열은 x배열보다 1 커야합니다.
    
    for i in range(bins):
        x[i] = i*dx + min_data
    #print(img.size)
    for j in img:
        #print(j)
        bin = int((j - min_data) / dx)
        #print(y)
        y[bin] += 1
    
    y[bins-2] += y[bins-1]
    y = y[:bins]

    plt.bar(x, y, width=dx)
    return np.column_stack((x, y))
for x in range(0,8 * 50):                          
    for y in range(0,8 * 50):
        if((x//50+y//50)%2==0):
            img_2[y, x] = 255
# for x in range(0,8):
#     for y in range(0,8):
#         if((x+y)%2==0):
#             img_2[y, x] = 255
            # cv2.rectangle(img_2, (50 * x, 50 * y), (50 * (x+1) - 1 , 50 * (y+1) - 1),(255), -1) #홀수행 (50,50) (50,150) , (50,250) , (50,350) 에서 점찍음
ksize=(3,3)
img_1_blur=cv2.blur(img_1,ksize)
img_2_blur=cv2.blur(img_2,ksize)
plt.figure(figsize=(12,8))
plt.subplot(3,2,1)
plt.imshow(img_1_blur,cmap='gray')
plt.subplot(3,2,2)
plt.imshow(img_2_blur,cmap='gray')
plt.subplot(3,2,3)
plt.hist(img_1.flatten(),255,[0,255])
plt.subplot(3,2,4)
plt.hist(img_2.flatten(),255,[0,255])
plt.subplot(3,2,5)
plt.hist(img_1_blur.flatten(), 256, [0,256]) 
plt.subplot(3,2,6)
plt.hist(img_2_blur.flatten(), 256, [0,256]) 

plt.show()