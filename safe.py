password = input('Давайте придумаем пароль: ')
def asc_password():
    tryy = 3
    while True:
        tps = input('Введите пароль ')
        if tps == password:
            print('пароль принят')
            exit()
        else:
            print('Отказано в доступе')
            tryy -= 1
            print(tryy)
            if tryy == 0:
                exit()
asc_password()