# -*- coding: utf-8 -*-
import threading
import jieba
import time
import re
import sys
import datetime
import cv2
from matplotlib import pyplot as plt
import numpy as np
import face_recognition
def face_video():
    face_img_jhc=face_recognition.load_image_file('./facesave/jhc.jpg')
    #face_img_jhc = face_recognition.load_image_file('jhc.jpg')
    face_img_jhc_encoding=face_recognition.face_encodings(face_img_jhc)[0]
    face_img_jj=face_recognition.load_image_file('./facesave/jj.jpg')
    #face_img_jj = face_recognition.load_image_file('jj.jpg')
    face_img_jj_encoding=face_recognition.face_encodings(face_img_jj)[0]
    all_face_enc=[
        face_img_jhc_encoding,
        face_img_jj_encoding
    ]
    all_face_name=[
        'jhc',
        'jj'
    ]
    if_recognition = True
    Video = cv2.VideoCapture(0)
    while(1):
        ret, frame = Video.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_loc=face_recognition.face_locations(rgb_small_frame)
        face_enc=face_recognition.face_encodings(rgb_small_frame,face_loc)
        for face_en in face_enc:
            matches=face_recognition.compare_faces(all_face_enc,face_en,tolerance=0.38)
            for name_num in range(len(matches)):
                if matches[name_num]:
                    name=all_face_name[name_num]
                    if name=='jhc':
                        return True
                else:
                    print('x')
                    break
        # cv2.imshow('1',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # cv2.imwrite('facesave\jhc2.jpg', frame)
            break
    Video.release()
    cv2.destroyAllWindows()

