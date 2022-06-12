# 함수 : 코드를 그룹짓는 기술, 직접 만드는 기능 
def 함수이름():
    # 함수를 사용했을때 작동시킬 코드 
    print("함수를 사용했습니다.")

def 함수이름2(number):
    print(number,"1번 함수 사용")

def 함수이름3(number, string):
    print(number,"1번 함수 사용",string)

def 함수이름4():
    print("함수4를 사용했습니다.")
    return "함수4"
# 소괄호 : 사용할 때 정해줄 값
# return : 사용한 곳에 알려줄 값 (반환값)
 
def 함수이름5(number):
    if number < 0:
        print("값은 0보다 작습니다")
        return -1               # 여기에서 종료 
    print("값은 0보다 큽니다.")
    return 1                    # 여기에서 종료 
    print("얘는 실행되지 않습니다.")


# 함수 사용 
# 함수이름3(1, "함수3")
# 함수이름3(2, "함수3")
# 함수이름3(3, 123)


# 리턴값 = 함수이름4()
# print(리턴값)

# 리턴값 = 함수이름5(-3)
# print(리턴값)

def star(num):
    i = "*"*num
    print(i)

     


# 함수 사용
star(4)     # ****
star(3)     # ***

# 제곱승 2,3 ==> 8
# 제곱승 3,3 ==> 27
# 제곱승 4,2 ==> 16
# 제곱승(2,3)       # **사용금지
def 제곱승(숫자1,숫자2):
    total = 1
    for i in range(숫자2):
        total = total * 숫자1
    print(total)

제곱승(2,3)
제곱승(2,2)
