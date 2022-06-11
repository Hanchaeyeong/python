import cv2

# 기능(코드를 저장)
def 이미지띄우기():
    img = cv2.imread("img1.jpg")
    cv2.imshow("title", img)
    cv2.waitKey(0)

def 이미지띄우기2(이미지이름):
    img = cv2.imread(이미지이름)
    cv2.imshow("title", img)
    cv2.waitKey(0)

def 회색이미지(이미지이름):
    img = cv2.imread(이미지이름)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("title", gray)
    cv2.waitKey(0)

# 함수사용
# 이미지띄우기()
# 이미지띄우기2("img1.jpg")
# 이미지띄우기2("img2.jpg")
# 회색이미지("img2.jpg")

# 변수 : 값저장, 함수 :코드저장 

