#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 迷宫问题, 状态空间探索
@Date: 2019-09-15 09:55:32
@Author: Ulysses
@LastEditTime: 2019-09-15 10:56:16
'''
from copy import deepcopy
from data_structures.stack_queue._queue import SQueue
from data_structures.stack_queue.stack import SStack

DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # 四个相邻的方向
# 0 可以通行, 1不可通行, 2已走过
MAZE = [[1] * 7, [1, 0, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1]]
MAZE_1 = deepcopy(MAZE)
MAZE_2 = deepcopy(MAZE)
START = (4, 1)
END = (4, 5)


def mark(maze, pos):
    """表示当前位置已走过"""
    maze[pos[0]][pos[1]] = 2


def passable(maze, pos):
    if pos[0] not in range(len(maze)) or pos[1] not in range(len(maze[0])):
        return False
    return maze[pos[0]][pos[1]] == 0


# 入口-出口 递归
# 从入口开始检查,
# 若当前为出口, 问题解决, 结束
# 当前位置无路可走, 探查失败, 按一定的方式检查其他路径
# 从可走的路径选择一个,继续探索


def find_path_rec(maze, pos, end):
    """使用递归的方式, 无需辅助结构"""
    mark(maze, pos)
    if pos == end:
        print(end, end=', ')
        return True
    for i in range(4):
        next_pos = pos[0] + DIRS[i][0], pos[1] + DIRS[i][1]
        if passable(maze, next_pos):  # 检查四邻是否能通行
            if find_path_rec(maze, next_pos, end):  # 递归检查
                print(pos, end=', ')
                return True
    return False


def find_path_stack(maze, start, end):
    """
    基于栈, 深度优先 deep-first 回溯法,栈保存信息
    2个基本动作, 前进: 当前位置存在尚未探寻的四邻, 选定一个方向开始探查;
    回溯: 四邻都探查过, 退回到最近记录的点, 若有尚未探查的点, 选定后探查,
    没有则删除这个点继续回溯上一个点, 所有点都查过,找不到出口则判为失败
    """
    if start == end:
        print(end, end=', ')
    st = SStack()
    mark(maze, start)
    st.push((start, 0))  # 入口, 探查方向DIRS[0]
    while not st.is_empty():
        pos, next_dir = st.pop()  # 最近检查的点和下一个方向
        for i in range(next_dir, 4):
            next_pos = (pos[0]+DIRS[i][0], pos[1]+DIRS[i][1])
            if next_pos == end:
                print_path_stack(end, pos, st)
                return
            if passable(maze, next_pos):
                st.push((pos, i+1))  # 原位置其他方向上的点
                mark(maze, next_pos)
                st.push((next_pos, 0))  # 当前点的下一个探查点
                break
    print("path not found")


def print_path_stack(end, pos, st):
    print(end, end=', ')
    print(pos, end=', ')
    while not st.is_empty():
        print(st.pop()[0], end=', ')


def find_path_queue(maze, start, end):
    if start == end:
        print(end, end=', ')
    q = SQueue()
    mark(maze, start)
    q.put((start, 0))  # 入口, 探查方向DIRS[0]
    path_dict = {start: None}  # 当前点: 前一个点
    while not q.is_empty():
        pos, next_dir = q.get()  # 最近检查的点和下一个方向

        for i in range(next_dir, 4):
            next_pos = (pos[0]+DIRS[i][0], pos[1]+DIRS[i][1])
            if next_pos == end:
                print_path_queue(end, pos, path_dict)
                return
            if passable(maze, next_pos):
                path_dict.update({next_pos: pos})
                q.put((pos, i+1))  # 原位置其他方向上的点
                mark(maze, next_pos)
                q.put((next_pos, 0))  # 当前点的下一个探查点
                break
    print("path not found")


def print_path_queue(end, pos, path_dict):
    print(end, end=', ')
    print(pos, end=', ')
    target = pos
    while target != START:
        for now, pre in path_dict.items():
            if now == target:
                print(pre, end=', ')
                target = pre
                break


if __name__ == "__main__":
    find_path_rec(MAZE, START, END)
    print('\n'+'-'*20+'\n')
    find_path_stack(MAZE_1, START, END)
    print('\n'+'-'*20+"\n")
    find_path_queue(MAZE_2, START, END)

    print('')
