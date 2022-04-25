#!/bin/python3

import os


def printFiles(p, space, f):
    dir = os.listdir(p)
    for i in dir:
        if i == "a.out":
            continue
        s = (' ' * space) + '- '
        if os.path.isfile(p + '/' + i):
            extension = i.split('.')[-1]
            if extension == i:
                continue
            if extension == "md":
                print(s + '[' + i + ']' + '(' + p + '/' + i + ')')
                f.write(s + '[' + i + ']' + '(' + p + '/' + i + ')' + '\n')
        else:
            print(s + i)
            f.write(s + i + '\n')
            printFiles(p + '/' + i, space + 2, f)


if __name__ == '__main__':
    file = "index.markdown"

    f = open(file, 'w')

    f.write("---\nlayout: default\ntitle: Home\n---\n")
    f.write('# Notes\n\n')

    # reasoning
    dir = ['ai', 'cd', 'cn', 'se', 'se-lab', 'wd', 'fa']
    # f.write('# Reasoning\n\n')
    space = 0
    for i in dir:
        if i == ".git" or i == ".vscode":
            continue
        s = (' ' * space) + '- '
        if not os.path.isfile(i):
            print(s + i)
            f.write(s + i + '\n')
            printFiles('./' + i, space + 2, f)
    f.write('\n\n')

    f.close()
