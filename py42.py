# page 146 (파이썬 지원함수)
print(2**3)         # 제곱승
print(4**2)         # 제곱승 

# 형변환 (자료형 바꾸기)
str(123)                    # 정수 123 -> 문자열 '123'
int('123')                  # 문자열 '123' -> 정수 123
float('123.0')              # 문자열 '123.0' -> 실수 123.0

result = eval('100-50')     # 정수 50
print(result)

# 149 page
# expr = input('계산식을 입력하세요>>>') 
# result = eval(expr)
# print(expr + '=' + str(result))

# abs == 절대값구하기 
print(abs(-3))
def 절대값구하기(num):
    if num <0:
        num*= -1
        return num
    return num


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(lst))
print(min(lst))

# divmod == % 
# pow == **

# round : 반올림
pi = 3.141592
print(round(pi,2))

# sum : 리스트 안에 있는 값을 전부 더하기해서  return
print(sum(lst))

# len : 리스트 항목의 갯수
print(len(lst))

# lst 평균
result = sum(lst)/len(lst)
print(result)

for i, j in enumerate(lst):
    print(i,":", j)
# enumerate : 방번호와 값을 분리 
# page 159, page 160 (1)
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for month, day in enumerate(months):
    print('{}월 = {}일'.format(month + 1, day))

color = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]
for number, c in enumerate(color):
    print('무지개의 {}번째 색은 {}입니다.'.format(number + 1,c))

months = []
for i in range (100):
    변수 = int(input("점수 입력>>>"))
    if 변수 < 0:
        break
    months.append(변수)
result = sum(months)/len(months)
print(result)
print(max(months))
print(min(months))

