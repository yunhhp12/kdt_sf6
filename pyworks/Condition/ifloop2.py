#다중 조건문

age = int(input("나이를 입력하세요: "))

if age < 20:
    print("미성년자입니다.")
elif 20 <= age < 30:
    print("20대입니다.")
elif 30 <= age < 40:
    print("30대입니다.")
else:
    print("늙늙")
print(f"나이는 {age}세 입니다.")