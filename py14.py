변수1 = 2+2    # 4

# 변수1 = 변수1 +2    # 변수1 = 4+2
변수1 += 2            # 누적연산
print(변수1)          # 6

a = 0
a += 1 
print(a)
a -= 1
print(a)

# page 76
piggy_bank = 0

money = 10000
piggy_bank += money
print('저금통에 용돈 {}원을 넣었습니다'.format(money))
print('지금 저금통에는 {}원이 있습니다'.format(piggy_bank))

snack = 2000
piggy_bank-=snack
print('저금통에서 스낵 구입비 {}원을 뺐습니다'.format(snack))
print('지금 저금통에는 {}원이 있습니다'.format(piggy_bank))

