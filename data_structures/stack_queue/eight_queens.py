#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 八皇后问题
@Date: 2019-09-16 22:19:53
@Author: Ulysses
@LastEditTime: 2019-09-16 22:30:43
'''

# 8*8的棋盘上, 任意2个皇后不能在同一横行,纵行或斜线上
# 1. 将二维的n*n的棋盘看成一维的数组a[n],其中a[i]代表第i行棋子所在的 列
# (一行只能有一个棋子)
# 2. 判断同列是否有其他棋子: a[i]不能与a中其他数相同
# 3. 判断正负对角线上是否有棋子, 特征2个棋子 行列值分别相减的绝对值相同


def queens(board, cur_line=0):
    if cur_line == len(board):
        print(board)
        return
    for col in range(len(board)):
        board[cur_line], flag = col, True  # 依次将棋子放置在某一列上
        for row in range(cur_line):  # 然后与已摆放的棋子进行检查
            if board[row] == col or abs(col - board[row]) == cur_line - row:
                flag = False
                break
        if flag:
            queens(board, cur_line + 1)


if __name__ == "__main__":
    queens([None]*8)
