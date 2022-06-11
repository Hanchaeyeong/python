# 함수
# 1. 개발자가 직접 만드는 기능(연산자)
# 2. 코드를 그룹짓는 기법


# def 첫인사():
    print('안녕하세요 저느 인천에 사는 000입니다.')
# def 본문() : 
    print('저는 인천에서 어쩌구저쩌구 00중학교를 다녔고 ~~~')
    print('저는 인천에서 어쩌구저쩌구 00고등학교를 다녔고 ~~~')
    print('저는 인천에서 어쩌구저쩌구 00대학교를 다녔고 ~~~')
    print('저는 인천에서 어쩌구저쩌구 00캠프를 다녔고 ~~~')
# def 끝인사() : 
    print('하여 저는 이 곳에 반드시 필요한 인재가 될 것 입니다.')

# 문제점 : 가독성이 매우 떨어짐 
# # 제목
'자기소개'
#  첫인사 
 첫인사()
# # 본문 
본문()
# 끝인사 
# 끝인사()        # 함수 사용 



def welcome():
    print('Hello Python')
    print('Nice to meet you')

welcome()

# page 188
def introduce(name, age):
    print('내 이름은 {}이고,나이는 {}입니다.'.format(name,age))

introduce('james,25')

# page 192
def address():
    str1 = "우편번호 12345\n"
    str1 += "서울시 영등포구 여의도동"
# 우편번호 12345
# 서울시 영등포구 여의도동 
    return str1

print(address())

# 함수에 입력해줄떄는 ()
# 함수로부터 결과를 받을떄는 return
# 함수를 만들땐 def 
# 함수를 사용할땐 함수이름과 소괄호 



