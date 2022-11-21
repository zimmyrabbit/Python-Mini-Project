import random

random_number = random.randrange(0,100)

game_count = 1

while True:
    my_number = int(input("1~100 사이의 숫자를 입력하세요 : "))

    if my_number > random_number:
        print("다운")
    elif my_number < random_number:
        print("업")
    elif my_number == random_number:
        print(f"{game_count} 회 만에 맞췄습니다.")
        break

    game_count += 1
