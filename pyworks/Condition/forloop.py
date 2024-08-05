#for 반복문
"""
for i range(시작값, 종료값+1, 증감값):
for i in list:
"""

a = range(10)
print(list(a))

b = range(1, 11)
print(list(b))

#초기값이 생략되면 0부터 시작
#끝값은 실제 끝값 - 1

c = range(1, 11, 2)
print(list(c))

#for문 1부터 10까지 출력
#for i in range (10):
#    print(i+1, end = ' ')

#for문 1부터 10까지 더하기
sum = 0
for i in range (10):
    sum += i
print(sum)