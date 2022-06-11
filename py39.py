# 입력한 돈으로 700원짜리 음료수 몇 잔을 뽑을 수 있는지 확인 
def vending_machine(money):
    can = 0 
    while money > 700:
        print("음료수 = {}개, 잔돈 = {}원".format(can, money))
        can += 1
        money -= 700
    print("음료수 = {}개, 잔돈 = {}원".format(can,money))


vending_machine(5000)

# money // 700 == 최대 갯수 

# 들어온 숫자를 절댓값(양수)으로 해서 더하기
def 절댓값더하기(숫자1, 숫자2):
    if 숫자1 < 0:
        숫자1 = 숫자1 * -1  
    if 숫자2 < 0:
        숫자2 = 숫자2 * -1
     
    return 숫자1+숫자2 

print(절댓값더하기(3, -1))          # 4 
print(절댓값더하기(5, 2))           # 7 
print(절댓값더하기(-3, -2))         # 5 


