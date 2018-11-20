# -*- coding: utf-8 -*-
import jieba
import time
import re
import sys
import datetime
import cv2
from matplotlib import pyplot as plt
import numpy as np
import face_recognition



def def_face_landmark():
    imgname1 = r'facesave\xtl.jpg'  # 文件
    imgname2 = '123.png'  # 文件
    color = (55, 255, 155)  # 颜色
    rad = 2  # 圆点半径
    img = cv2.imread(imgname2)
    # img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    face_loc = face_recognition.face_landmarks(img)
    for dic_in_face in face_loc:
        for i in dic_in_face['chin']:
            cv2.circle(img, i, rad, color, -1)
        for i in dic_in_face['left_eyebrow']:
            cv2.circle(img, i, rad, color, -1)
        for i in dic_in_face['right_eyebrow']:
            cv2.circle(img, i, rad, color, -1)
        for i in dic_in_face['nose_bridge']:
            cv2.circle(img, i, rad, color, -1)
        for i in dic_in_face['nose_tip']:
            cv2.circle(img, i, rad, color, -1)
        for i in dic_in_face['left_eye']:
            cv2.circle(img, i, rad, color, -1)
        for i in dic_in_face['right_eye']:
            cv2.circle(img, i, rad, color, -1)
        for i in dic_in_face['top_lip']:
            cv2.circle(img, i, rad, color, -1)
        for i in dic_in_face['bottom_lip']:
            cv2.circle(img, i, rad, color, -1)


    cv2.namedWindow("识别")
    cv2.imshow("识别", img)
    cv2.waitKey(0)
def def_face_compare():
    k_img=face_recognition.load_image_file('123.png')
    unk_img=face_recognition.load_image_file('2.png')
    k_face_encoding=face_recognition.face_encodings(k_img)[0]
    #print('k_face_encoding:{}'.format(k_face_encoding))
    unk_face_encoding=face_recognition.face_encodings(unk_img)[0]
    #print('unk_face_encoding:{}'.format(unk_face_encoding))
    k_face=[k_face_encoding]
    results=face_recognition.compare_faces(k_face,unk_face_encoding,tolerance=0.4)
    print('result:{}'.format(results))
def def_face_video():
    face_img1=face_recognition.load_image_file(r'facesave\jj.png')
    face_img1_encoding=face_recognition.face_encodings(face_img1)[0]
    face_img2=face_recognition.load_image_file(r'facesave\jhc.jpg')
    face_img2_encoding=face_recognition.face_encodings(face_img2)[0]
    face_img3=face_recognition.load_image_file(r'facesave\xtl.jpg')
    face_img3_encoding=face_recognition.face_encodings(face_img3)[0]
    all_face_enc=[
        face_img1_encoding,
        face_img2_encoding,
        face_img3_encoding
    ]
    all_face_name=[
        '林俊杰',
        'jhc',
        'xtl'
    ]
    if_recognition = True
    Video = cv2.VideoCapture(0)
    while(1):
        ret, frame = Video.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_loc=face_recognition.face_locations(rgb_small_frame)
        face_enc=face_recognition.face_encodings(rgb_small_frame,face_loc)
        #face_names=[]
        for face_en in face_enc:
            matches=face_recognition.compare_faces(all_face_enc,face_en,tolerance=0.45)
            for name_num in range(len(matches)):
                if matches[name_num]:
                    name=all_face_name[name_num]
                    print(name)
                    # font = cv2.FONT_HERSHEY_DUPLEX
                    # cv2.putText(frame, name, (0,25), font, 1.0, (255, 0, 0), 1)
                    #face_names.append(name)
                else:
                    name="x"
                    print(name)
                    # font = cv2.FONT_HERSHEY_DUPLEX
                    # cv2.putText(frame, name, (0, 25), font, 1.0, (255, 0, 0), 1)


        # for (top, right, bottom, left), name in zip(face_loc, face_names):
        #     top *= 4
        #     right *= 4
        #     bottom *= 4
        #     left *= 4
        #
        #     # cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
        #     #
        #     # cv2.rectangle(frame,(left,bottom-35),(right,bottom),(255,0,0),2)
        #     font = cv2.FONT_HERSHEY_DUPLEX
        #     cv2.putText(frame,name,(left+6,bottom-6),font,1.0,(255,255,255),1)
        color = (55, 255, 155)  # 颜色
        rad = 2  # 圆点半径
        face_land=face_recognition.face_landmarks(small_frame)
        img=frame
        for dic_in_face in face_land:
            for i in dic_in_face['chin']:
                tup1=i[0]*4
                tup2=i[1]*4
                tup=(tup1,tup2)
                cv2.circle(img, tup, rad, color, -1)
            for i in dic_in_face['left_eyebrow']:
                tup1=i[0]*4
                tup2=i[1]*4
                tup=(tup1,tup2)
                cv2.circle(img, tup, rad, color, -1)
            for i in dic_in_face['right_eyebrow']:
                tup1=i[0]*4
                tup2=i[1]*4
                tup=(tup1,tup2)
                cv2.circle(img, tup, rad, color, -1)
            for i in dic_in_face['nose_bridge']:
                tup1=i[0]*4
                tup2=i[1]*4
                tup=(tup1,tup2)
                cv2.circle(img, tup, rad, color, -1)
            for i in dic_in_face['nose_tip']:
                tup1=i[0]*4
                tup2=i[1]*4
                tup=(tup1,tup2)
                cv2.circle(img, tup, rad, color, -1)
            for i in dic_in_face['left_eye']:
                tup1=i[0]*4
                tup2=i[1]*4
                tup=(tup1,tup2)
                cv2.circle(img, tup, rad, color, -1)
            for i in dic_in_face['right_eye']:
                tup1=i[0]*4
                tup2=i[1]*4
                tup=(tup1,tup2)
                cv2.circle(img, tup, rad, color, -1)
            for i in dic_in_face['top_lip']:
                tup1=i[0]*4
                tup2=i[1]*4
                tup=(tup1,tup2)
                cv2.circle(img, tup, rad, color, -1)
            for i in dic_in_face['bottom_lip']:
                tup1=i[0]*4
                tup2=i[1]*4
                tup=(tup1,tup2)
                cv2.circle(img, tup, rad, color, -1)
        cv2.imshow('1',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    Video.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
    #def_face_landmark()
    #def_face_compare()
    def_face_video()
    cv2.destroyAllWindows()




