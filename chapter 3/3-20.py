BABA_체력=100
print(f"BABA_체력: {BABA_체력}")
while BABA_체력>0:
    데미지=None
    while True:
        데미지=int(input("가할 데미지(데미지가 0이면 턴을 넘김): "))
        if 데미지<0:
            print("가할 데미지는 최소 0입니다.")
            continue
        elif 데미지==0:
            print("턴을 넘깁니다.")
        elif 데미지<=20:
            print("효과는 미미했다.")
            break
        elif 데미지<=30:
            print("효과는 굉장했따.")
            break
        else:
            print("효과는 치명적이었다.")
            break
    BABA_체력=BABA_체력-데미지
    if BABA_체력<0:
        BABA_체력=0
    print(f"BABA가 공격받아 체력 {BABA_체력}이 남았습니다.")
    if BABA_체력<=0:
        print(f"BABA가 쓰러졌습니다.")