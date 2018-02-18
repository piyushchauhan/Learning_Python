theBoard = {'low-L': ' ',
            'low-M': ' ',
            'low-R': ' ',
            'mid-L': ' ',
            'mid-M': ' ',
            'mid-R': ' ',
            'top-L': ' ',
            'top-R': ' ',
            'top-M': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def check(key1, key2, key3):
    return key1 == key2 and key2 == key3 and key2 != ' '


def checkFinish(board):
    # top row
    if check(board['top-L'], board['top-M'], board['top-R']):
        return True

    # mid row
    elif check(board['mid-L'], board['mid-M'], board['mid-R']):
        return True

    # low row
    elif check(board['low-L'], board['low-M'], board['low-R']):
        return True

    # L col
    elif check(board['top-L'], board['mid-L'], board['low-L']):
        return True

    # R col
    elif check(board['top-R'], board['mid-R'], board['low-R']):
        return True

    # M col
    elif check(board['top-M'], board['mid-M'], board['low-M']):
        return True

    # top-L to low-R cross
    elif check(board['top-L'], board['mid-M'], board['low-R']):
        return True

    # top-R to low-L cross
    elif check(board['top-R'], board['mid-M'], board['low-L']):
        return True

    else:
        return False


Instrutions = '''
Hello there
To make a move type in the following text:
top-L:top left
top-M:top mid
top-R:top right
mid-L:mid left
mid-M:mid mid
mid-R:mid right
low-L:low left
low-M:low mid
low-R:low right
'''
print('Welcome to Tic-Tac-Toe Board')
print(Instrutions)

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    var=checkFinish(theBoard)
    if var:
        print('The winner is '+turn)
        break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    var=checkFinish(theBoard)
printBoard(theBoard)
print('The game is over. Thank You for playing')
