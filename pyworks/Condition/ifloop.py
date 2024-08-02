#if문 - 조건: 나이가 15세 이상이면 "관람가"라고 출력
#구문 만들때 끝에 콜론(:) 집어넣고 다음줄에 들여쓰기

age = 13

'''
if age >= 15:
    print("관람가")
print(f"나이는 {age}세 입니다.")
'''

if age >= 15:
    print("관람가")
else:
    print("관람불가")
print(f"나이는 {age}세 입니다.")

#입력 수가 짝수인지 홀수인지 판별하는 프로그램
num = int(input("t숫자를 입력하세요:"))

if num % 2 == 0:
    print("짝수")
else:
    print("홀수")
print(f"입력된 수는 {num}입니다.")