#n진수 표현하기
num = 10 #10진수
binary_num = 0b1010
hex_num = 0xA

print(num)
print(f"2진수 0b1010의 10진수는 {binary_num}")
print(hex_num)

#진수 표현 함수
#bin() : binary, 10진수 들어가면 2진수로 표현
#hex() : hexa, 10진수 들어가면 16진수로 표현
print(bin(10))
print(bin(65))
print(hex(10))

#아스키 코드값:
#ord(문자)
#chr(코드값)

print(ord('0'))
print(ord('B'))
print(chr(48))

#복합 대입 연산자
val = 1

val += 10
val -= 10
val *= 10
val /= 10
print(val)

#청바지 수량
jean = 0
msg = "" #empty string

jean += 1
print(f"청바지 수량: {jean}")
