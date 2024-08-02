#비교 연산 - >, <, >=, <=, ==, !=
#비교 연산의 결과는 - bool자료 (True/False)
b1 = 2 > 1

print(b1) #True
print(type(b1))

b2 = (2 == 1)
print(b2)

b3 = (2 != 1)
print(b3)

#논리 연산 - and, or, not
#and - 2가지 이상의 조건에서 모두 참일 때는 참
#or - 2가지 이상의 조건에서 하나만 참이어도 참
logic1 = (2 > 1) and (2 == 1)
print(logic1)

logic2 = (2 > 1) or (2 == 1)
print(logic2)

logic3 = not (2 != 1)
print(logic3)

#논리 연산 예제
age = 18
under20 = age < 20
print(under20)
print(not under20)