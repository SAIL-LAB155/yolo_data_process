
'''
cut several videos into frames within a floder
'''

import cv2
import os
pathin = '/home/hkuit164/Downloads/basketball'
pathout = '/home/hkuit164/Downloads/tmp/'
# count=0
for video in os.listdir(pathin):
    video_path = os.path.join(pathin, video)
    print(video_path)
    step = 1
    cnt = 0
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if ret:
            if cnt % step == 0:
                cv2.imwrite(pathout +video.split('.')[0]+'__'+ str(cnt) + ".jpg", frame)
            cnt += 1
        else:
            break
