my_shop = ["반팔티", "청바지", "이어폰", ["무선키보드", "유선키보드"]]

#이어폰 출력
print(my_shop[2])

#반팔티를 긴팔티로 수정
my_shop[0] = "긴팔티"
print(my_shop)

#리스트 내 리스트 인덱싱
#이차원 리스트: 행과 열로 구성됨
print(my_shop[-1])
print(my_shop[-1][0])

#여러개 삭제
del my_shop[0:2]
print(my_shop)

