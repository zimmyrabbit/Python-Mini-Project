import random

random_number = random.randrange(0,100)

game_count = 1

while True:
    try:
        my_number = int(input("1~100 사이의 숫자를 입력하세요 : "))

        if (my_number > 100) or (my_number < 1):
            raise Exception("1~100 사이 숫자만 입력 가능합니다.")
            continue

        if my_number > random_number:
            print("다운")
        elif my_number < random_number:
            print("업")
        elif my_number == random_number:
            print(f"{game_count} 회 만에 맞췄습니다.")
            break

        game_count += 1
    except ValueError:
        print("숫자를 입력하세요")
    except Exception as e:
        print("***", e)
    except:
        print("other Error") 

