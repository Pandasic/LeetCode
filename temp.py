import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret,im = cap.read()
    cv2.imshow("or",im)
    gray =cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",gray)
    hist = cv2.calcHist([gray],[0],None,[256],[0,256])
    hist_pair = list(enumerate(hist))
    hist_pair.sort(key = lambda x:x[1])
    max_arr = [hist_pair[0][0]]
    for i in range(1,len(hist_pair)):
        if len(max_arr) == 1:
            if abs(max_arr[-1] - hist_pair[i][0])>50:
                max_arr += [hist_pair[i][0]]
        if len(max_arr) == 2:
            if abs(max_arr[0] - hist_pair[i][0])>50 \
            and abs(max_arr[1] - hist_pair[i][0])>50:
                max_arr += [hist_pair[i][0]]
        if len(max_arr) == 2:

            break
    max_arr.sort(key = lambda x:x)
    print(max_arr)
    m1 = (max_arr[0]+max_arr[1])/2
    #m2 = min(hist[max_arr[1]:max_arr[2]])
    print(m1)
    gray[gray<m1] = 0
    gray[gray>m1] = 255
    #gray[int(m1)<gray & gray<int(m2)] = 127
    cv2.imshow("gray2",gray)
    cv2.waitKey(10)