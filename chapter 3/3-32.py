"""""
[__맞짱떠__]
1. User's Monster 객체 생성
2. Opponent's Monster 객체 생성(CPU)
3. 전투 초기화
4. User의 공격 기술 선택
5. User's Monster가 Opponent's Monster 선빵. 상대도 공격
6. 서로 한 턴에 공격을 한번씩 주고받는다. 먼저 몬스터 체력이 0 이 되어 쓰러지면 게임이 종료
""" ""

import random
import os
import sys
import time
from utils.display import delay_print


def initial_display():
    print("=" * 30)
    print("뒷골목에 오신 것을 환영합니다.")
    monsters = ["화끈이", "축축이", "풀떼기"]
    for index, monster in enumerate(monsters):
        print(f"[{index+1}] {monster}\t", end=" ")

    while True:
        try:
            selected_num = input("\n플레이할 몬스터의 번호를 선택해 주세요. >>")
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
    print(f"[{selected_num}] {user_monster}를 선택하셨습니다. ")
    print(f"{user_name}님 환영합니다. ")

    return user_monster


class Monster:
    def __init__(self, name, types, skills, EVs, health="===================="):
        self.name = name
        self.types = types
        self.skills = skills
        self.attack = EVs["공격력"]  # 공격력 능력치(Effort Value)
        self.defense = EVs["방어력"]  # 방어력 능력치(Effort Value)
        self.evasion = round(
            random.uniform(0.1, 0.3), 4
        )  # 회피율 랜덤지정. round(실수,n): 소숫점 n자리까지 반올림 표현
        self.health = health
        self.bars = 20


def create_monster(monster):
    if monster == "화끈이":
        return Monster("화끈이", "불", ["불꽃뿜기", "불똥싸기", "몸통박치기"], {"공격력": 4, "방어력": 2})
    elif monster == "축축이":
        return Monster("축축이", "물", ["비눗방울 불기", "흐느적거리기", "적시기"], {"공격력": 2, "방어력": 4})
    elif monster == "풀떼기":
        return Monster("풀떼기", "풀", ["가지치기", "꽃가루날리기", "나뭇잎댄스"], {"공격력": 3, "방어력": 3})


def initial_fight(home_monster, away_monster):
    print("===============맞짱 시작===============")
    print(f"\n[{home_monster.name}]")
    print("타입/", home_monster.types)
    print("공격력/", home_monster.attack)
    print("방어력/", home_monster.defense)
    print("회피율/", home_monster.evasion)
    print("\n VS \n")
    print("타입/", away_monster.types)
    print("공격력/", away_monster.attack)
    print("방어력/", away_monster.defense)
    print("회피율/", away_monster.evasion)

    attrs = ["불", "물", "풀"]
    string_1_attack = ""
    string_2_attack = ""
    for index, value in enumerate(attrs):
        if home_monster.types == value:
            if home_monster.types == value:
                string_1_attack = "\n효과는 평범했다."
                string_2_attack = "\n효과는 평범했다."

            # away_monster 속성이 더 강력할 때
            if away_monster.types == attrs[(index + 1) % 3]:
                away_monster.attack *= 2
                away_monster.defense *= 2
                string_1_attack = "\n효과가 별로인 듯 하다..."
                string_2_attack = "\n효과는 매우 뛰어났다!!!"

            # home_monster 속성이 더 강력할 때
            if away_monster.types == attrs[(index + 2) % 3]:
                home_monster.attack *= 2
                home_monster.defense *= 2
                string_1_attack = "\n효과는 매우 뛰어났다!!!"
                string_2_attack = "\n효과가 별로인 듯 하다!..."

        fight(home_monster, away_monster, string_1_attack, string_2_attack)


def fight(home_monster, away_monster, string_1_attack, string_2_attack):
    while (home_monster.bars > 0) and (away_monster.bars > 0):
        print(f"[User][{home_monster.name}]\t{home_monster.health}")
        print(f"[Opnt]][{away_monster.name}]\t{away_monster.health}")  # Opponent
        turn(home_monster, away_monster, string_1_attack, True)
        turn(away_monster, home_monster, string_2_attack, False)


def turn(home_monster, away_monster, effective, is_user):
    if is_user:
        print(f"가랏!!! {home_monster.name}!")
    else:
        print(f"{away_monster}가 공격해 왔다!")

    for index, value in enumerate(home_monster.skills):
        print(f"{index+1}", value)

    if is_user:
        while True:
            try:
                skill_index = int(input("무엇을 할까? >> "))
                if skill_index - 1 in range(len(home_monster.skills)):
                    break
                else:
                    print("뭐라고? >> ")

            except:
                print("뭐라고? >> ")
    else:
        skill_index = random.randint(0, 2)  # 상대방이 할 행위 무작위 선택
    delay_print(f"\n{home_monster.name}! {home_monster.skills[skill_index-1]}!!")
    time.sleep(1)

    # 회피율 기준으로 공격이 빗나가면 체력을 소모하지 않는다.
    if random.uniform(0, 1) < away_monster.evasion:
        delay_print(f"\n{away_monster.name}는 재빠르게 피했다!")
    else:
        # 체력을 깎음. 방어력 높을 때 away_monster.bars가 증가하지 않도록 주의
        delay_print(effective)
        away_monster.bars -= home_monster.attack - (0.3 * away_monster.defense)

    away_monster.health = ""  # 초기화 이후 다시 할당

    # 체력 업데이트 이후 출력
    for _ in range(int(away_monster.bars)):
        away_monster.health += "="

    time.sleep(1)
    os.system("cls")

    # 체력 게이지 소모 후 맞짱 종료
    if away_monster.bars <= 0:
        delay_print(f"\n[{home_monster.name}] 승리...")
        delay_print(f"\n[{away_monster.name}] 패배... 루저자식...")
        sys.exit(0)


if __name__ == "__main__":
    user_monster = create_monster(initial_display())
    other_monster = create_monster("축축이")

    print(vars(user_monster))
    print(vars(other_monster))

    initial_fight(user_monster, other_monster)
