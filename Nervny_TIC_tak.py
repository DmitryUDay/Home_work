p1 = []
p2 = []
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    # [0,1,-1], #debug_nichya
    # [-1,1,1],
    # [-1,-1,1]

]
def motematichka():
    for _ in range(3):
        for row in board:
            if 1 in row:
                row[row.index(1)] = ' X '
            if -1 in row:
                row[row.index(-1)] = ' O '
            if 0 in row:
                row[row.index(0)] = '  '
    print('-'*16)
    print(f'| {board[0][0]} | {board[0][1]} | {board[0][2]} |')
    print('-'*16)
    print(f'| {board[1][0]} | {board[1][1]} | {board[1][2]} |')
    print('-'*16)
    print(f'| {board[2][0]} | {board[2][1]} | {board[2][2]} |')
    print('-'*16)

def chBoard():
        if board[0][0]==' X ' and board[1][1]==' X ' and board[2][2] == ' X ':
            print('крестик выйграл по диагонали с лева!')
            exit()
        if board[0][0] == ' O ' and board[1][1] == ' O ' and board[2][2] == ' O ':
            print('Нолик выйграл по диагонали с лева!')
            exit()

        if board[0][2]==' X ' and board[1][1]==' X ' and board[2][0] == ' X ':
            print('крестик выйграл по диагонали с права!')
            exit()
        if board[0][2]==' O ' and board[1][1]==' O ' and board[2][0] == ' O ':
            print('Нолик выйграл по диагонали с права!')
            exit()

        if board[0][0]==' X ' and board[1][0]==' X ' and board[2][0] == ' X ':
            print('крестик выйграл по прямой линии с первого столбца!')
            exit()
        if board[0][0]==' O ' and board[1][0]==' O ' and board[2][0] == ' O ':
            print('нолик выйграл по прямой линии с первого столбца!')
            exit()

        if board[0][1]==' X ' and board[1][1]==' X ' and board[2][1] == ' X ':
            print('крестик выйграл по прямой со второго ряда столбца!')
            exit()
        if board[0][1]==' O ' and board[1][1]==' O ' and board[2][1] == ' O ':
            print('нолик выйграл по прямой со второго ряда столбца!')
            exit()
        
        if board[0][2]==' X ' and board[1][2]==' X ' and board[2][2] == ' X ':
            print('крестик выйграл по прямой с третьего ряда столбца!')
            exit()
        if board[0][2]==' O ' and board[1][2]==' O ' and board[2][2] == ' O ':
            print('нолик выйграл по прямой с третьего ряда столбца!')
            exit()
        
        if board[0][0] == ' X ' and board[0][1] == ' X ' and board[0][2] == ' X ':
            print('крестик выйграл по вертикали с первого ряда!')
            exit()
        if board[0][0]==' O ' and board[0][1]==' O ' and board[0][2] == ' O ':
            print('нолик выйграл по вертикали с первого ряда!')
            exit()

        if board[1][0]==' X ' and board[1][1]==' X ' and board[1][2] == ' X ':
            print('крестик выйграл по вертикали со второго ряда!')
            exit()
        if board[1][0]==' O ' and board[1][1]==' O ' and board[1][2] == ' O ':
            print('нолик выйграл по вертикали со второго ряда!')
            exit()

        if board[2][0]== ' X ' and board[2][1]== ' X ' and board[2][2] == ' X ':
            print('крестик выйграл по вертикали с третьего ряда!')
            exit()
        if board[2][0] == ' O ' and board[2][1] == ' O ' and board[2][2] == ' O ':
            print('нолик выйграл по вертикали с третьего ряда!')
            exit()

while True:
        p1 = strok = int(input("Х, Введите номер столбца: "))
        stolb = int(input("Теперь номер строки: "))
        if strok > 3:
            print('неверные значения!')
        else:
            if stolb > 3:
                print('неверные значения!')
            else:
                board[stolb-1][strok-1] = 1
                motematichka()
                chBoard()
                p2 = strok = int(input("0, Введите номер столбца: "))
                stolb = int(input("Теперь номер строки: "))
                if strok > 3:
                    print('неверные значения!')
                else:
                    if stolb > 3:
                        print('неверные значения!')
                    else:
                        board[stolb-1][strok-1] = -1
                        motematichka()
                        chBoard()