# 온도 : 20도이하 => 추움
# 온도 : 21~28 => 정상
# 온도 : 282도 초과 => 더움 

# print(온도) #1. 추움 2. 정상 3. 더움 ==> 불가능

# 외부 조건에 따라서 내 프로그램 동작을 다르게 
# 조건문 (if)
온도 = float(input("온도를 입력하세요>>>"))
if 온도 > 28: 
    print("온도가")
    print("덥다")
if 온도 > 21 and 온도 <= 28:
    print("온도가")
    print("정상")
if 온도 <= 21:
    print("온도가")
    print("춥다")
print('프로그램 끝')
'''
if 조건:
    조건이 맞으면 실행할 문장

'''
