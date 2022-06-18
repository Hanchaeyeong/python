# 두 수의 합
def Sum(a,b):
    result = a+b
    print(result)

a = 3
b = 2
result = a + b
print(result)
a = 6
b = 3



# 코드가 길어지면 지저분!!

sum(2,3)
sum(6,3)
# 초보자가 사용하기 편하게 변수와 함수를 뭉쳐놓고 쉽게 제공하자 
class 사칙연산:
    a,b = 0,0
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def 더하기(self):
        result = a+b
        print(result)
    def 빼기(self):
        result = a-b
        print(result)
    def 곱하기(self):
        result = a*b
        print(result)
    def 나누기(self):
        result = a/b
        print(result)

객체1 = 사칙연산(3,5)
객체1.빼기()

class 더하기:
    # 두개더하기
    def 두개더하기(self,a,b):
        print(a+b)
        return a+b
    # 세개더하기
    def 세개더하기(self,a,b,c):
        print(a+b+c)
        return a+b+c
    # 네개더하기 
    def 세개더하기(self,a,b,c,d):
        print(a+b+c+d)
        return a+b+c+d
    def __init__(self):     # 생성자 
        print("처음에 무조건 사용됨")
    def __del__(self):
        print("끝날때 무조건 사용됨")

객체2 = 더하기()
객체2.세개더하기(3,4,5)
# page 277 예제 


    




