# 예제1)

from queue import PriorityQueue
from sqlalchemy import false
from sympy import print_maple_code


if True:
    print('맞습니다.')
if false:
    print('틀립니다')
if 22 > 21:
    print('22가 21보다 컸었나?')

# 예제2)

age = int(input("당신의 나이는 몇살입니까?"))
if age >=20:
    print("당신은 성인 입니다.")
elif age < 20 and age > 13:
    print("당신은 청소년 입니다.")
elif age > 0 and age <= 13:
    print("어린이 입니다.")
else:
    print("?")

# 예제 3)

체온 = int(input("온도를 입력해주세요: "))
if 체온 < 35.0:
    print("저체온증!! 얼른 119에 전화하세요!")
elif 체온 <= 37.5:
    print("정상 체온입니다.")
elif 체온 < 45.0:
    print("체온이 높습니다. 설마 코로나?")
else:
    print("?")


# 1 
# 100~90 : A, 89~80 : B, ....
점수 = int(input("점수를 입력하세요>>>"))
if 점수 < 60:
    print('점수는',점수,'점이고, 학점은 F학점입니다.')
elif 점수 < 70:
     print('점수는',점수,'점이고, 학점은 D학점입니다.')
elif 점수 < 80:
     print('점수는',점수,'점이고, 학점은 C학점입니다.')
elif 점수 < 90:
     print('점수는',점수,'점이고, 학점은 B학점입니다.')
elif 점수 <= 100:
     print('점수는',점수,'점이고, 학점은 A학점입니다.')
else:
    print('?')

# 2 
정수 = input('정수를 입력하세요>>>')
 if 정수 % 3 == 0:
     print(정수,'는 3의 배수입니다.')
else:
    print(정수,'는 3의 배수가 아닙니다.')

# 3
while True:
    정수1 = int(input('정수1 입력>>>))
    정수2 = int(input('정수2 입력>>>))
    정수3 = int(input('정수3 입력>>>))

    if 정수1 >= 정수2 and 정수1 >= 정수3:
        print('가장 큰 수는',정수1,'입니다.')
    elif 정수2 >= 정수2 and 정수2 >= 정수3:
        print('가장 큰 수는',정수2,'입니다.')
    else:
        print('가장 큰 수는',정수3,'입니다.')