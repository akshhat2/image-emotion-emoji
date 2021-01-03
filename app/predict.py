import tkinter as tk
# from tkinter import *
import cv2
from PIL import Image, ImageTk
import os
import numpy as np
import tensorflow as tf


 
# load the tokenizer
def predict(fname):

  # pre-define the max sequence length (from traini
  # load the model
  model = tf.keras.models.load_model('app\\models\\model2.h5')
  cv2.ocl.setUseOpenCL(False)

  emotion_dict = {0: "   Angry   ", 1: "Disgusted", 2: "  Fearful  ", 3: "   Happy   ", 4: "  Neutral  ", 5: "    Sad    ", 6: "Surprised"}
  # print(fname)
  frame1=cv2.imread("app\\static\\css\\temp5.jpg",1)
  print(frame1,"******************")
  # frame1 = cv2.resize(img,(500,400))

  bounding_box = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
  gray_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
  num_face = bounding_box.detectMultiScale(gray_frame,scaleFactor=1.3, minNeighbors=5)
  # show_text=[0]
  for (x, y, w, h) in num_face:
    cv2.rectangle(frame1, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
    roi_gray_frame = gray_frame[y:y+h, x:x+w]
    cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)
    prediction = model.predict(cropped_img)
    maxindex = int(np.argmax(prediction))
  return maxindex
    