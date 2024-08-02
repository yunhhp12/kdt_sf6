'''
유용한 문자열 함수
    len(): 개수
    count(): 특정 문자 개수
    upper(): 대문자 변환
    lower(): 소문자 변환
    split(): 문자열을 잘라서 리스트로 반환
    replace(): 문자 바꾸기
'''

f = "바나나"
print(len(f))
print(f.count("나"))

upper_case = "hello world".upper()
print(upper_case)

strlist = "hello world"
print(strlist.split())

friends = "존 루나 체리"
print(friends.split())

alpha = "a:b:c:d"
print(alpha.split(":"))

#replace()
msg = "Hello Python"
print(msg.replace("Python", "C++"))

