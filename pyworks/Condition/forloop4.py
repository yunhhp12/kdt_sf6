shop = ["반팔티", "바지", "이어폰", "키보드"]

#마우스 추가
shop.append('마우스')

#이어폰 삭제
shop.remove("이어폰")

#리스트 여러 요소 추가
shop.extend(["커피", "비스켓"])

for i in shop:
    print(i)

#리스트의 연산
#갯수, 합계, 평균, 최대값, 최소값

score = [70, 80, 60, 98, 40]
print(len(score))
total = 0
for i in score:
    total += i
    print(total)
total2 = sum(score)
print(total2)

print(f"갯수: {len(score)}")
print(f"합계: {sum(score)}")
print(f"평균: {len(score) / len(score)}")
print(f"최댓값: {max(score)}")
print(f"최소값: {min(score)}")