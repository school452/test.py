from time import sleep
from msvcrt import getch
while True:
    print()
    print("_______________________________________________________")
    maxb = int(input("Введите максимальный балл за тест: "))
    print()
    print(f"Баллов на оценку 5 - от {maxb*85//100} до {maxb}")
    print(f"Баллов на оценку 4 - от {maxb*65//100} до {(maxb*85//100)-1}")
    print(f"Баллов на оценку 3 - от {maxb*45//100} до {(maxb*65//100)-1}")
    print(f"Баллов на оценку 2 - от 0 до {(maxb*45//100)-1}")
    print()
    print("Для выхода нажмите [E]")
    print("Для того, чтобы запустить программу ещё раз нажмите [C]")
    pressedKey = getch()
    if pressedKey == b'e' or pressedKey == b'\xe3':
        break
    elif pressedKey == b'c' or pressedKey == b'\xe1':
        continue
    else:
        print(f'Ошибка, запустите программу ещё раз')
        sleep(3)
        break
