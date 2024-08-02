#문자열은 특별한 1차원 리스트이다.
say = "have a nice day!"

print(say[0])

#nice day!
print(say[7:])

#문자열 포맷 서식
# %d - 정수, %s - 문자열, %f - 실수
print("나는 이번 달에 책을 %d권 샀어요" %2)
print("나는 이번 달에 책을 %s 권 샀어요" %'두')

count = 2
cost = 50000
print("이번 달에 책을 %d권 샀고, 비용은 %d원 들었어요" %(count, cost))

#단위 변환
print("1인치는 %.2fcm 입니다" %2.54)
#f포맷 방식
inch = 2.540000
print(f"1인치는 {inch:.2f}cm 입니다.")