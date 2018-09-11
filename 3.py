# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:32:53 2017

@author: ZHENGHAN ZHANG
"""

#first define an empty board(row,column)
def make_board(m, n, filler):    
    y=[]
    for i in range(m):
        x=[]
        for j in range(n):
            x.append(filler)
        y.append(x)
    return y

#visualization of the board
def print_board(board):
    rows=len(board)
    columns=len(board[0])
    for i in range(rows):
        print('+---' * columns,'+',sep='')
        m=''
        for j in range(columns):
            m+='| '
            m+= str(board[i][j])
            m+=' '
        m+='|'        
        print(m)
    print('+---' * columns,'+',sep='')
    return

#board initiation by user input
def mainMakeBoard():
    a=input('Enter the rows and columns (row,column):').split(',')
    b=input('Please enter the filler:(enter space by default)')
    x=make_board(int(a[0]),int(a[1]),b)
    print_board(x)
    return x


#user interface    
def UI(x):
    a=input('Enter the rows and columns (row,column):').split(',')
    b=input('Please enter the filler:(enter space by default)')
    c=input("Please enter the decorator:(enter 'x' or 'o')")
    y=update_board(x,a[0],a[1],c,b)
    print_board(x)
    return [y,c]

def update_board(board, i, j, decorator, filler):
    if decorator != filler:
        board[int(i)-1][int(j)-1]=decorator
        x=1
    else:
        print('You cannot overwrite an existing space!')
        x=0
    return bool(x)

#winner algorithm
def is_horizontal_winner(board, decorator):
    for j in range(len(board[0])):
        m=0
        for i in range(len(board)):
            m+=int(bool(board[i][j]==decorator))
        if m == len(board):
            print('You win by column',j+1)
            return True
    return 

def is_vertical_winner(board, decorator):
    for i in range(len(board)):
        m=0
        for j in range(len(board[0])):
            m+=int(bool(board[i][j]==decorator))
        if m == len(board[0]):
            print('You win by row',i+1)
            return True
    return



def is_diagonal_winner(board, decorator):
    if len(board) != len(board[0]):
        return
    else:
        m=0
        for i in range(len(board)):
            m+=int(bool(board[i][i]==decorator))
        if m == len(board):
            print('You win by diagonal!')
            return True
    return

def iswinner(board, decorator):
    if is_horizontal_winner(board, decorator) == True:
        return True
    elif is_vertical_winner(board, decorator) == True:
        return True
    elif is_diagonal_winner(board, decorator) == True:
        return True
    
#main function    
def main():
    x=mainMakeBoard()        
    i=1
    while True:        
        if i%2 == 1:
            print("It is Player 1's turn.")
            y=UI(x)            
            if y[0] == True:
                i+=1
            #then for every loop check if the winner is here
            if iswinner(x,y[1]) == True:
                print('Player 1 is victorious!')
                break
        else:
            print("It is Player 2's turn.")
            y=UI(x)
            if y[0] == True:
                i+=1
            if iswinner(x,y[1]) == True:
                print('Player 2 is victorious!')
                break
        
    
    
if __name__ == '__main__':
    main()
    