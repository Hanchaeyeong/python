#출력
print('hello 파이썬')
print('hi 파이썬')
print(123)

# 변수(저장공간)
언어 = '파이썬'
언어_2 = '자바'

# 변수 출력
print(언어)
print('Hello ', 언어, '반갑습니다')
print('Hello {} 반갑습니다 {}.'.format(언어,언어_2))

# 출력
변수1 = input('변수1에 넣을 값 : ')
변수2 = input('변수2에 넣을 값 : ')
print(변수1+변수2)
print(int(변수1)+int(변수2))

# 조건문 
if int(변수1) < 10:
    print('변수1은 10보다 작습니다')
elif int(변수1) < 20:
    print('변수1은 10이상 20미만입니다')
else:
    print('변수1은 20이상입니다')