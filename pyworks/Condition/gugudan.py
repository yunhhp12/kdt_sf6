#구구단 3단 출력
#dan = int(input("단을 입력하여 주세요: "))

#for i in range(1, 11):
#    mult = i * dan
#    print(f"{dan} x {i} = {mult}")

#2중 for loop
for i in range(2,10):
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}", end = " ")
    print() #행바꿈

#2중 for loop
for i in range(1, 5):
    for j in range(1, 6 - i):
        print(f"*", end = " ")
    print() #행바꿈

#왼쪽 공백
for i in range(1, 5):
    print(" " * (4 - i) + "*" * i)