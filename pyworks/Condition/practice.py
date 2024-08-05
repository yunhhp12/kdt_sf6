vending_machine = ["게토레이", "레쓰비", "생수", "이프로"]

while True:
    print("=" * 15 + " RESTART")
    choice = input("마시고 싶은 음료?")

    if choice in vending_machine:
        vending_machine.remove(choice)
        print(f"{choice} 드릴게요\n")
    else:
        print(f"{choice}는 지금 없네요\n")

    if len(vending_machine) == 0:
        print("이제 자판기내 음료가 없어요. 나중에 다시 찾아주세요.")
        break