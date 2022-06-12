import cv2
import mediapipe as mp

# 이미지에서 얼굴찾기 
cap = cv2.VideoCapture("img3.jpg")

mpDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils 
faceDetection = mpDetection.FaceDetection(0.40)      # 60% 이상 얼굴로 인식될경우

success, img = cap.read()
if success:
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(img,detection)
cv2.imshow("my title" , img)
cv2.waitKey(0)