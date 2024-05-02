#!/usr/bin/env python
# coding: utf-8

# In[ ]:


myBoard = {'7': ' ', '8': ' ', '9': ' ',
           '6': ' ', '5': ' ', '4': ' ',
           '1': ' ', '2': ' ', '3': ' '}
keys = []


def printmyBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def start():
    char = 'X'
    count = 0
    for i in range(10):
        printmyBoard(myBoard)
        print("It's " + char + " your turn. Move to which place:")

        move_char = input()

        if myBoard[move_char] == ' ':
            myBoard[move_char] = char
            count += 1
        else:
            print("It's already filled.\nMove to another place:")
            continue
        if count >= 5:
            if myBoard['7'] == myBoard['8'] == myBoard['9'] != ' ':
                printmyBoard(myBoard)
                print("\nGame Completed.\n")
                print(" **** " + char + " won. ****")
                break
            elif myBoard['4'] == myBoard['5'] == myBoard['6'] != ' ':
                printmyBoard(myBoard)
                print("\nGame Completed.\n")
                print(" **** " + char + " won. ****")
                break
            elif myBoard['1'] == myBoard['2'] == myBoard['3'] != ' ':
                printmyBoard(myBoard)
                print("\nGame Completed.\n")
                print(" **** " + char + " won. ****")
                break
            elif myBoard['1'] == myBoard['4'] == myBoard['7'] != ' ':
                printmyBoard(myBoard)
                print("\nGame Completed.\n")
                print(" **** " + char + " won. ****")
                break
            elif myBoard['2'] == myBoard['5'] == myBoard['8'] != ' ':
                printmyBoard(myBoard)
                print("\nGame Completed.\n")
                print(" **** " + char + " won. ****")
                break
            elif myBoard['3'] == myBoard['6'] == myBoard['9'] != ' ':
                printmyBoard(myBoard)
                print("\nGame Completed.\n")
                print(" **** " + char + " won. ****")
                break
            elif myBoard['7'] == myBoard['5'] == myBoard['3'] != ' ':
                printmyBoard(myBoard)
                print("\nGame Completed.\n")
                print(" **** " + char + " won. ****")
                break
            elif myBoard['1'] == myBoard['5'] == myBoard['9'] != ' ':
                printmyBoard(myBoard)
                print("\nGame Completed.\n")
                print(" **** " + char + " won. ****")
                break
        if count == 9:
            print("\nGame Completed.\n")
            print("It's a Tie!!!")

        if char == 'X':
            char = 'O'
        else:
            char = 'X'
    replay = input("Do want to play again?(y/n)")
    if replay == "y" or replay == "Y":
        for key in keys:
            myBoard[key] = " "
        start()


if __name__ == "__main__":
    start()

