score = int(input("점수 입력: "))

if score >= 90:
    print("A 등급입니다.")
elif 80 <= score < 90:
    print("B 등급입니다.")
elif 70 <= score < 80:
    print("C 등급입니다.")
elif 60 <= score < 70:
    print("D 등급입니다.")
else:
    print("E 등급입니다.")