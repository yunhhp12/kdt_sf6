#실습1: 사용자가 입력한 수까지 정수의 합 계산 (홀수의 합만 구하기)
user_range = int(input("어디까지 계산할까요?"))

odd_sum = 0
for i in range(user_range+1):
    if i % 2 == 1:
        odd_sum += i
    else:
        pass
print(f"홀수의 합계: {odd_sum}")