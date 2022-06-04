# # for  변수명 in range(10):

# # while 
# import time

# from sympy import prime 

# 기준점 = 0
# while 기준점<10:
#     time.sleep(1)       # 1초동안 멈춤
#     print('10은 5보다 큽니다.')
#     기준점 += 1      
# print('프로그램 종료')
# '''
# while 조건:
#     조건이 맞을때마다 실행할 코드 
# '''
# num = 1
# while num < 11:
#     print(num,"번 했습니다.")
#     num += 1

# 105page
# n = 10
# while n > 0:
#     print(n,"번 했습니다.")
#     n -= 1

# # 111page (1)
# 변수1 = int(input('정수를 입력하세요>>>'))
# 기준점 = 0
# if  기준점 <=0:
#     print('잘못된 입력입니다.')
# while 기준점<변수1:       
#     print(기준점+1,'번째 hello')
#     기준점 += 1      

# 111page (2)

'''
(1) 1~100 출력
(2) if문을 써서 7의 배수만 출력되게 바꾸기 
'''
기준점 = 1
while 기준점 <=100:
    if 기준점 % 7 ==0:
        print(기준점)
    기준점 += 1


