score = [10, 20, 30, 40]

print(score)

#인덱싱: 특정 요소 접근
print(f"인덱싱 예제: {score[2]}")

#슬라이싱: 여러개 요소 접근
print(f"슬라이싱 예제1: {score[:3]}") #0부터 2번 요소까지 접근
print(f"슬라이싱 예제2: {score[3:]}") #3번째 요소부터 끝까지 접근
print(f"슬라이싱 예제3: {score[:]}") #전 요소 접근

#요소 수정
score[1] = 50
print(f"요소 수정 예제: {score}")

#요소 삭제
del score[2]
print(f"요소 삭제 예제: {score}")