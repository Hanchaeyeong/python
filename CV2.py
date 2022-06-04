import cv2

# 이미지 불러오기
이미지 = cv2.imread('img1.jpg')

# 이미지 보여주기(제목,이미지명)
cv2.imshow("title", 이미지)

# 이미지 띄워놓고 대기
cv2.waitKey(0)
