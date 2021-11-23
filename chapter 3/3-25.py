def select_monster():
    print("몬스터 리그에 오신 것을 환영합니다.^^")
    monsters = ["화끈이", "축축이", "풀떼기"]  # list

    for index, monster in enumerate(
        monsters
    ):  # 열거하다. 순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴
        print(f"[{index+1}] {monster}\t", end=" ")

    # 사용자로부터 몬스터(숫자.인덱스) 입력받음
    selected_num = input('\n플레이할 "몬스터"의 번호를 선택해 주세요.: ')

    # 게임 플레이어의 이름 입력받음
    user_name = input("당신의 이름을 입력해 주세요.: ")

    # 사용자가 선택한 몬스터 출력
    user_monster = monsters[int(selected_num) - 1]
    print(f"[{selected_num}] {user_monster}를 선택하셨습니다. ")
    print(f"{user_name}님 환영합니다. ")


if __name__ == "__main__":
    select_monster()
