#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 八皇后问题
@Date: 2019-09-16 22:19:53
@Author: Ulysses
@LastEditTime: 2019-09-18 20:19:59
'''
from data_structures.stack_queue.stack import SStack
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


def is_valid(board, col):
    """将下一行棋子放在col列是否可行"""
    next_row = len(board)
    for line in range(next_row):
        if board[line] == col or abs(board[line] - col) == next_row - line:
            return False
    return True


def gen_queens(num, state=()):
    """
    递归,生成器
    Args:
        num ([type]): num*num棋盘
        state (tuple, optional): 所有皇后位置
    """
    for col in range(num):
        if is_valid(state, col):
            if len(state) == num - 1:
                yield (col,)
            else:
                for result in gen_queens(num, state+(col,)):
                    yield (col,) + result


def queens_stack(check_board):
    st = SStack()
    st.push([0, ()])  # 当前棋子所在列, [每行棋子所在列]
    while not st.is_empty():
        now_queue = st.pop()
        cur_col = now_queue[0]
        # 每一新行 棋子都从0列开始摆放
        # 回溯旧行 从原先的下一列开始
        for col in range(cur_col, len(check_board)):
            pos = now_queue[1]  # 运行到此行时的位置记录
            if is_valid(pos, col):
                # 每一个解对应一个pos路径元组, 在压栈出栈过程中要保持不变
                if len(pos) == len(check_board) - 1:
                    pos += (col,)
                    print(pos)
                else:
                    new_col = col + 1
                    now_queue[0] = new_col  # 把棋子放在下一列是否有解
                    st.push(now_queue)
                    new_pos = pos + (col,)  # 生成新的 下一行棋子 从第0列开始
                    st.push([0, new_pos])


if __name__ == "__main__":
    queens([None]*4)
    print("-"*30)
    print(len(list(gen_queens(8))))
    print("-"*30)
    for item in gen_queens(4):
        print(item)
    print("-"*30)
    queens_stack([None]*4)
