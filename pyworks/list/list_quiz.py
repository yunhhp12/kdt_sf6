#실습1

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]

#1. 2번 인덱스값 출력
print(rainbow[2])

#2. 알파벳 순서로 정렬한 값 출력
rainbow.sort()
print(rainbow)

#3. 좋아하는 색 맨 마지막에 추가하기
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"] #초기화용
rainbow.append("white")
print(rainbow)

#4. 3~6번째 값 삭제하기
rainbow.pop() #3번에서 추가한거 삭제
del rainbow[2:6]
print(rainbow)
