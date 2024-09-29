theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,

'4': ' ' , '5': ' ' , '6': ' ' ,

'1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)
    

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])

    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

    print('-+-+-')
    
def game():
    turn = 'X'
    count = 0
    
    for i in range(10):
        printBoard(theBoard)
        print("Its your turn," + turn + "Move to which place?")
        
        move = input()
        
        if theBoard[move] ==' ':
            theBoard[move]=turn
            count = count + 1
            
        else:
            print("That place is already filled.\nMove to which place?")
            continue