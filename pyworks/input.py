#입력함수 - input(문자열)

name = input("이름 입력: ")
print(f"당신의 이름은 {name}이군요.")

int_num = 10.5
print(int_num)

print(int(10.5))

#오류 처리 (try ~except 구문)
# :(콜론) - 코드 블럭 ({})
# 다음 줄에서는 4칸 띄어쓰기 (indent)
#try:
#    실행문 (오류가 나올 수 있는 구문)
#except:
#    오류를 처리할 수 있는 구문


try:
    num1 = input("첫 번째 수 입력:")
    num2 = input("두 번째 수 입력:")
    print(int(num1) + int(num2))
except:
    print("정수를 입력하여 주세요.")

