import cv2
import numpy as np
import matplotlib.pyplot as plt

# def DFT(x):

#     N = len(x)# period(every interval) of x
#     n = np.arange(N)
#     k = n.reshape((N, 1))
#     W = np.exp(-2j * np.pi * k * n / N)
    
#     X = np.dot(W, x)#convolutuon of vector e
    
#     return X
# def IDFT(X):

#     N = len(X)# period(every interval) of x
#     n = np.arange(N)
#     k = n.reshape((N, 1))
#     W_ = np.exp(2j * np.pi * k * n / N)
    
#     x = 1/N*(np.dot(W_, X))#convolutuon of vector e
    
#     return x

# def FFT(x):
#     x = np.asarray(x, dtype=complex)
#     N = len(x)
#     if N == 1:
#         return x
#     if N % 2 != 0:
#         raise ValueError("the input size must be 2^n")
#     else:
#         X_even = FFT(x[::2])
#         X_odd = FFT(x[1::2])
#         W = np.exp(-2j*np.pi*np.arange(N)/ N)
         
#         X = np.concatenate([X_even+W[:int(N/2)]*X_odd,X_even+W[int(N/2):]*X_odd])
#         return X

# def IFFT(X):
#     N = len(X)
    
#     if N == 1:
#         return X
#     else:
#         x_even = IFFT(X[::2])
#         x_odd = IFFT(X[1::2])
#         W_ = np.exp(2j*np.pi*np.arange(N)/ N)
         
#         x = (np.concatenate([x_even+W_[:int(N/2)]*x_odd, x_even+W_[int(N/2):]*x_odd]))
#         return (1/2) * x


# def FFT2D(x):
#     height, width = x.shape[0], x.shape[1]
#     #X =np.zeros(x.shape)
#     X =np.zeros(x.shape,dtype=complex)
#     if len(X.shape) == 2:
#         for i in range(height):
#             X[i, :] = FFT(x[i, :])

#         for i in range(width):
#             X[:, i] = FFT(X[:, i])
#     return X

# def IFFT2D(X):
#     height, width = X.shape[0], X.shape[1]
#     x =np.zeros(X.shape,dtype=complex)
#     #X =np.zeros(x.shape)

#     if len(X.shape) == 2:
#         for i in range(height):
#             x[i, :] = IFFT(X[i, :])

#         for i in range(width):
#             x[:, i] = IFFT(x[:, i])
#     x=np.real(x) #Image data of dtype complex128 cannot be converted to float
#     return x

# """ 
# newly knowed knowledge
# np.linespace(start,end,n) : Divide the start and end points by n intervals.

# """
# x = np.linspace(0, 20, 201) #0~20을 201개 구간(0.1)로 나눕니다.
# y = np.sin(x)
# # sampling rate
# sr = 128
# # sampling interval
# ts = 1.0/sr
# t = np.arange(0,1,ts)

# freq = 1.
# x = 3*np.sin(2*np.pi*freq*t)

# freq = 4
# x += np.sin(2*np.pi*freq*t)

# freq = 7   
# x += 0.5* np.sin(2*np.pi*freq*t)
# """ 
# stem(x,y,use_line_collection = True)

# stemlines.set_visible(False) ## stem line 안보이게
# baseline.set_visible(False) ## base line 안보이게
# markers.set_color('red')# 색상 고를 수 있게
# stemlines.set_linestyle('--') #라인 스타일 바꿀 수 있게
# stemlines.set_color('purple') #라인 색깔 바꿀 수 있게 해줌
# """

# X = DFT(x)
# # calculate the frequency
# # sampling rate is 100 and interval is 0.01

# N = len(X)
# n = np.arange(N)
# print("lenth of N: ",N)
# print("component of N: ",n)

# T = N/sr #because function is unperiodic, we can guess T equals to 1
# freq = n/T #frequency is 100 

# plt.figure(figsize = (8, 4))
# plt.stem(freq, abs(X), 'b', \
#          markerfmt=" ", basefmt="-b")
# plt.xlabel('Freq (Hz)')
# plt.ylabel('DFT Amplitude |X(freq)|')
# plt.show()

# n_oneside = N//2
# # get the one side frequency
# f_oneside = freq[:n_oneside]

# # normalize the amplitude
# X_oneside =X[:n_oneside]/n_oneside

# plt.figure(figsize = (8, 4))
# plt.subplot(121)
# plt.stem(f_oneside, abs(X_oneside), 'b', \
#          markerfmt=" ", basefmt="-b")
# plt.xlabel('Freq (Hz)')
# plt.ylabel('DFT Amplitude |X(freq)|')

# plt.subplot(122)
# plt.stem(f_oneside, abs(X_oneside), 'b', \
#          markerfmt=" ", basefmt="-b")
# plt.xlabel('Freq (Hz)')
# plt.xlim(0, 10)
# plt.tight_layout()
# plt.show()