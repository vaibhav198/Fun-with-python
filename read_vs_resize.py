import time
import cv2

#Sometimes a small fraction of time matters when we are deploying the project/model in production, so we need to keep in mind
#very small-small factor like either we should read the image in required size or resize the image after reading.

t1 = time.time()
img = cv2.imread("img.jpg")
T1 = time.time() - t1
print("read time {}".format(T1))

t2 = time.time()

img1 = cv2.resize(img, (360, 640))

T2 = time.time() - t2

print("resize time: {}".format(T2))

print("Comparision in factor/times: {}".format(T1/T2))