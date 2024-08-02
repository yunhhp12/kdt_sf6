#리스트 함수

#추가 - append(), insert()
#삭제 - pop(), remove()

lower = ["a", "b", "c", "d"]

#e 추가
lower.append("e") #맨 뒤에 삽입
print(lower)

#e 삭제
lower.pop() #맨 뒤 삭제
print(lower)

#b와 c 사이에 e 추가
lower.insert(2, 'e')
print(lower)

#c 삭제
lower.remove('c')
print(lower)