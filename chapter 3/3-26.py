def select_monster():
    print("몬스터 리그에 오신 것을 환영합니다.^^")
    monsters = ["화끈이", "축축이", "풀떼기"]  # list

    for index, monster in enumerate(
        monsters
    ):  # 열거하다. 순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴
        print(f"[{index+1}] {monster}\t", end=" ")

    count = 0

    while True:
        try:
            # 사용자의 숫자를 입력받습니다.
            selected_num = input('\n플레이할 "몬스터"의 번호를 선택해 주세요.: ')
            user_monster = monsters[int(selected_num) - 1]
        except ValueError:
            print("올바르지 않은 값입니다.")
        except IndexError:
            print("올바르지 않은 번호입니다.")
        except Exception as e:
            print(e)
        else:
            user_name = input("당신의 이름을 입력해 주세요.: ")
            break
        finally:
            count += 1
            print(f"{count}회 입력을 시도했습니다.")
    print(f"[{selected_num}] {user_monster}를 선택하셨습니다. ")
    print(f"{user_name}님 환영합니다. ")


if __name__ == "__main__":
    select_monster()
