# -*- coding: utf-8 -*-
import threading
import ChatUMain as chat
import FaceURecognition as FaceRec
if __name__=="__main__":
    FaceRec.face_video()
    chat.Chat()

#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple face_recognition