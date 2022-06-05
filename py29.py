# 1. 리스트 
Ist =[]             # 리스트 변수 선언

# 추가하기 
Ist.append(3)
Ist.append(3.14)
Ist.append('안녕하세요')

# 삽입하기(중간에 추가)
Ist.insert(1, "1번에 추가")

# 수정하기
Ist[1] = "1번방 수정"

# 제거하기
Ist.pop(-1)         # -값은 뒤에서부터 계산, (앞에서부터는 0부터, 뒤에서부터는 -1부터)

# 잘라내기 
print(Ist[0:2])     # 0 ~ 1까지 잘라냄

for i in Ist:    
    print(i,end=", ")

# page 129(3)
입력값 = int(input("몇 개의 과일을 보관할까요?>>>"))
리스트 = []
for i in range(입력값): 
    과일 = input('{}번째 과일을 입력하세요>>>'.format(i+1))
    리스트.append(과일)
print('입력받은 과일들은 {} 입니다.'.format(리스트))

