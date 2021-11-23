class Monster:
    def __init__(self, name, attack, defence):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.hp = 20
        print(f"{name}가 생성되었습니다.")

    def decrease_hp(self, hp):
        self.hp = self.hp - hp
        print(f"\n{self.name}의 체력이 {hp}만큼 감소했습니다.")
        print(f"{self.name}의 남은 체력: {self.hp} \n")

    def show_info(self):
        print(f"Monster Name: {self.name}")
        print(f"Monster Attack: {self.attack}")
        print(f"Monster Defense: {self.defence}")
        print(f"Monster HP: {self.hp} \n")

    def __del__(self):
        print(f"{self.name} 객체가 제거되었습니다.")


if __name__ == "__main__":
    화끈이 = Monster("화끈이", 4, 2)
    불끈이 = Monster("불끈이", 3, 3)
    화끈이.decrease_hp(2)
    화끈이.show_info()
    불끈이.show_info()
