import random
import pandas as pd
from copy import deepcopy
import numpy as np







def generateBoard():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    iboard = []
    for x in range(6):
        curr = []
        for y in range(6):
            curr.append(('a',True))
        iboard.append(curr)
    for x in range(1,5):
        for y in range(1,5):
            iboard[x][y] = (random.choice(letters), False)
    return iboard

def genBoardfromString(string):
    vals = [x for x in string]
    vals = np.array(vals)
    vals = vals.reshape((4,4))
    vals = vals.tolist()
    board = []
    for x in range(6):
        curr = []
        for y in range(6):
            curr.append(('a',True))
        board.append(curr)
    for x in range(1,5):
        for y in range(1,5):
            board[x][y] = (vals[x-1][y-1], False)
    return board

def generateSolutions(iboard):

    shortWordsSet = list(pd.read_csv('short_sorted.csv').squeeze())
    dictionary = {}
    for vals in shortWordsSet:
        if vals[0] in dictionary:
            dictionary[vals[0]].append(vals)
        else:
            dictionary[vals[0]] = [vals]
    def recur(words, board, xcurr, ycurr, word_len):
        if not words:
            return []
        checks = []
        for x in range(-1,2):
            for y in range(-1,2):
                _, used = board[xcurr + x][ycurr + y]
                if not used:
                    checks.append((xcurr + x, ycurr + y))
        new_dict = {}
        arr = []
        for x in words:
            if len(x) == word_len:
                arr.append(x)
                continue
            if x[word_len] in new_dict:
                new_dict[x[word_len]].append(x)
            else:
                new_dict[x[word_len]] = [x]
        if not checks:
            return [x for x in words if len(x)== word_len]
        for x, y in checks:
            ourboard = deepcopy(board)
            val, _ = ourboard[x][y]
            ourboard[x][y] = (val, True)
            arr += recur(new_dict.get(val,[]),ourboard,x,y,word_len + 1)
        return arr
    eeeeks = []
    for x in range(1,5):
        for y in range(1,5):
            aaa = deepcopy(iboard)
            a, _ = aaa[x][y]
            aaa[x][y] = (a, True)
            eeeeks.extend(recur(dictionary.get(iboard[x][y][0],[]),aaa,x,y,1))
    for x in range(1,5):
        line = ''
        for y in range(1,5):
            line += (iboard[x][y][0] + ' ')
    return eeeeks

def findWords():
    letters = input("Enter the letters with no spaces all together as one word ie abcdef: ")
    board = genBoardfromString(letters)
    sols = generateSolutions(board)
    sols.sort(key = len, reverse = True)
    a = [x for x in sols if len(x)>=3]
    print(set(a))

def main():
    findWords()
main()