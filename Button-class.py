clc = 0
cnt = 0
while True:
    class button:
        def click(self):
            global clc
            clc += 1
            print('Кол-во нажатий: ', clc, 'колво занчения: ', cnt)
        def click_count(self):
            global cnt
            cnt += 1
        def reset(self):
            global clc,cnt
            vibor = input('1|всё, 2|кол-во нажатий, 3|число нажатий ')
            if vibor == '1':
                clc, cnt = 0,0
                print('Клики: ', clc)
                print('Нажатия: ', cnt)
            elif vibor == '2':
                cnt = 0
                print('нажатия: ', cnt)
            elif vibor == '3':
                clc = 0
                print('Клики: ', clc)
        def clear(self):
            print('\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n')

            #---проверка действий---
    print('add|reset|count|cls')
    vib = input('Выберите действие: ')
    if vib == 'add':
        add = button()
        add_cnt = button()
        add_cnt.click_count()
        add.click()

    elif vib == 'cls':
        class_cls = button()
        class_cls.clear()
    elif vib == 'count':
        print(cnt,'нажатий')
    elif vib == 'reset':
        resetr = button()
        resetr.reset()