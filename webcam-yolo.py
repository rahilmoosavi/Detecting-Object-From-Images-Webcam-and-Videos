from ultralytics import YOLO
import cv2
model=YOLO('yolov8l.pt')

cap=cv2.VideoCapture(0)
while True:
    s,img=cap.read()
    result=model(img,show=True)
    cv2.waitKey(1)