리스트 = []
세트 = set({})
튜플 = ()

리스트.append(1)
리스트.append(2)
리스트.append(2)
print(리스트)

# set 추가하기(중복불가)
세트.add(1)
세트.add(2)
세트.add(2)
# set 제거하기
세트.discard(2)
print(세트)

튜플 = tuple(리스트)
print(튜플)

세트 = set({})
# page 67 (4)
for i in range(3):
    여행지 = input("희망하는 수학여행지를 입력하세요>>>")
    세트.add(여행지)
print("조사된 수학여행지는 {}입니다.".format(세트))
