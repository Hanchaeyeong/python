import py45
import py46

# 238 (1)
nation = ["그리스","아테네","독일", "베를린", "러시아", "모스크바", "미국","워싱턴"]
idx = 0
py45.메모장쓰기('')

for i in nation:
    if idx %2 == 0:
        print("국가는",i)
        py45.메모장추가쓰기(i)
    else:
        print("수도는",i)
        py45.메모장추가쓰기("-"+i+"\n")
    idx += 1