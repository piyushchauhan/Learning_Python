#! python3
import os
import pprint
import pyperclip

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(grid[j][i], end='')
    print()


def char2grid(string):
    lists = string.split(os.linesep)
    finalList = []
    for x in range(len(lists)):
        finalList.append(list(lists[x]))
    return finalList


pprint.pprint(char2grid(pyperclip.paste()))
for i in range(len(char2grid(pyperclip.paste()))):
    for j in range(len(grid[i])):
        print(grid[j][i], end='')
    print()
