#실습1

#조건 1 - 자동차의 시내 주행 속도가 50km/hr 이상이면 속도 위반 출력
#조건 2 - 아니면 규정 속도 준수!! 출력

speed = int(input("주행 속도:"))

if speed >= 50:
    print("속도 위반")
else:
    print("규정 속도 준수!!")
print(f"주행 속도는 {speed}km 입니다.")
