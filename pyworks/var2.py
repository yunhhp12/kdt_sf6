"""
변수 선언 (변수명)
1. 숫자로 시작하면 안됨
2. 공백 있으면 안됨
3. 특수문자 사용 불가능 (몇 개 제외: _)

에러
1. 실행전 에러 (컴파일 오류) -> 에디터가 미리 알려줌
2. 실행후 에러 (런타임 에러) -> 

"""

season2 = "여름"
season = "summer"
age = 13

#print(season2)
#print(age)

print('*** 회원가입 ***')
user_id = "kdt6"
user_pw = 'sf1234'
email = 'jerry@korea.com'
age = 35

print(f'아이디: {user_id}')
print(f'비밀번호: {user_pw}')
print(f'Email: {email}')
print(f'Age: {age}')

#소수점 처리하기
n1 = 10
n2 = 3
div = n1 / n2
print(f"10 나누기 3 결과값: {div}")
print(f"10 나누기 3 결과값 타입: {type(div)}")
print(f"10 나누기 3 결과값 소숫점 둘째자리까지 표시: {div:0.2f}")
print(f"10 나누기 3 결과값 소숫점 둘째자리까지 표시: {round(div, 2)}")

#반올림 함수 - round (숫자, 자리수)
print(round(1.647, 1))
