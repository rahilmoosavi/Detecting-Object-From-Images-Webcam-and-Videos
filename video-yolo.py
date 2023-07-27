from ultralytics import YOLO
import cv2
model=YOLO('yolov8l.pt')

video_path ='videos/input_video.mp4'
cap = cv2.VideoCapture(video_path)

while True:
    s,img=cap.read()
    result=model(img,show=True)
    cv2.waitKey(1)