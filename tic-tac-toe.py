from random import randrange

boardGlobal = [[1, 2, 3], [4 , 5, 6], [7, 8, 9]]
boardGlobal[1][1] = 'X'


#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
def DisplayBoard(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', board[0][0], '  |  ', board[0][1], '  |  ', board[0][2], '  |' )
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', board[1][0], '  |  ', board[1][1], '  |  ', board[1][2], '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', board[2][0], '  |  ', board[2][1], '  |  ', board[2][2], '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
def EnterMove(board):

    while True:
        movimiento = int(input('[!] Introduzca su movimiento (del 1 al 9): '))
        if movimiento == 1:
            if board[0][0] != 'X' and board[0][0] != 'O':
                board[0][0] = 'O'
                return board
            else: 
                print('[!] Introduce un movimiento valido')        
        elif movimiento == 2:
            
            if board[0][1] != 'X' and board[0][1] != 'O':
                board[0][1] = 'O'
                return board
            else: 
                print('[!] Introduce un movimiento valido')        
        elif movimiento == 3:
            
            if board[0][2] != 'X' and board[0][2] != 'O':
                board[0][2] = 'O'
                return board
            else: 
                print('[!] Introduce un movimiento valido')        
        elif movimiento == 4:
            
            if board[1][0] != 'X' and board[1][0] != 'O':
                board[1][0] = 'O'
                return board
            else: 
                print('[!] Introduce un movimiento valido')        
        elif movimiento == 5:
            
            if board[1][1] != 'X' and board[1][1] != 'O':
                board[1][1] = 'O'
                return board
            else: 
                print('[!] Introduce un movimiento valido')        
        elif movimiento == 6:
            
            if board[1][2] != 'X' and board[1][2] != 'O':
                board[1][2] = 'O'
                return board
            else: 
                print('[!] Introduce un movimiento valido')        
        elif movimiento == 7:
            
            if board[2][0] != 'X' and board[2][0] != 'O':
                board[2][0] = 'O'
                return board
            else: 
                print('[!] Introduce un movimiento valido')        
        elif movimiento == 8:
            
            if board[2][1] != 'X' and board[2][1] != 'O':
                board[2][1] = 'O'
                return board
            else: 
                print('[!] Introduce un movimiento valido')        
        elif movimiento == 9:
            
            if board[2][2] != 'X' and board[2][2] != 'O':
                board[2][2] = 'O'
                return board
            else: 
                print('[!] Introduce un movimiento valido')        
        
    DisplayBoard(board)
        
    

#
# la función examina el tablero y construye una lista de todos los cuadros vacíos
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#
def MakeListOfFreeFields(board):
    FreeFields = []

    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                FreeFields.append((i, j))

    return FreeFields

#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#
def VictoryFor(board, sign):

    # Horizontal

    for i in range(3):
        match = 0
        for j in range(3):
            if board[i][j] == sign:
                match += 1
        if match == 3:
            return True

    # Vertical
    for i in range(3):
        match = 0
        for j in range(3):
            if board[j][i] == sign:
                match += 1
        if match == 3:
            return True

    # Diagonal

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign or \
       board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    else:
        return False


#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#
def DrawMove(board):
    camposLibres = MakeListOfFreeFields(board)
    movimientoMaquina = randrange(len(camposLibres))
    # print('Movimiento de la maquina:',movimientoMaquina)
    fila, columna = camposLibres[movimientoMaquina]
    # print('Fila y columna:', fila, columna)
    board[fila][columna] = 'X'
    DisplayBoard(board)

    return board

# main
#
DisplayBoard(boardGlobal)

while True:
        
    boardGlobal = EnterMove(boardGlobal)
    
    if VictoryFor(boardGlobal,'O'):
        print('[+] Enhorabuena, has ganado')
        break
    
    boardGlobal = DrawMove(boardGlobal)
    
    if VictoryFor(boardGlobal,'X'):
        print('[+] Has perdido')
        break
    
    if len(MakeListOfFreeFields(boardGlobal)) == 0:
        print('[+] Empate, la partida ha terminado')
        break
        
