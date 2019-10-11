#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 最短路径问题
@Date: 2019-10-02 09:47:54
@Author: Ulysses
@LastEditTime: 2019-10-11 17:22:08
'''
from data_structures.tree.prioqueue import PrioQueue
from data_structures.graph.graph import GraphAL, inf
from pprint import pprint

def dijkstra_shortest_paths(graph, v0):
    """
    DiJkstra单源点最短路径, 从一个点到其他各个点的最短路径
    最短路径中前段也是最短路径：要记录V0到各顶点的最短路径，只需要记录V0到v的
    前一个顶点
    Args:
        graph ([type]): 图
        v0 ([type]): 源点
    复杂度: 时间 O(|E|log|E|), 空间O(|E|)
    """
    vnum = graph.vertex_num()
    assert 0 <= v0 < vnum
    paths = [None] * vnum  # 记录最短路径 （前一顶点v', v0到v最短路径长度）
    count = 0
    # 初始队列  (v0经v到v'的最短已知长度, v, v前一顶点v')
    cands = PrioQueue([(0, v0, v0)])
    while count < vnum and not cands.is_empty():
        plen, u, vmin = cands.dequeue()  # 取具有最小p值的边
        if paths[vmin]:  # vmin在U里,最短路径已知，继续
            continue
        paths[vmin] = (u, plen)  # 记录最新确定的最短路径
        for v, w in graph.out_edges(vmin):  # 经过u的vmin的邻接边
            if not paths[v]:  # 未知的最短路径的顶点路径(端点一个在U一个在V-U)
                cands.enqueue((plen + w, vmin, v))   # 队列中添加新的路径
                # v0到v距离要更新, 可以
        count += 1
    return paths


def all_shortest_paths(graph):
    """
    任意顶点间最短路径 Floyd算法，基于图的邻接矩阵A
    n个顶点的图 G = (V, E)
    - 边(v, v')∈E, 顶点v到v'的路径, 长度为A[v][v'], 无边时看做长度为∞的直接路径
    - v到v'的直接路径未必最短, 途径其他顶点的路径可能更短
    - 检查和比较v到v'的可能经过的任何顶点的所有路径, 找出最短路径
    递推生成一系列n*n方阵 Ak(0<=k<=n),Ak[i][j]表示从vi到vj的途径顶点可为v0,
    v1,...,vk-1的最短路径长度
    A0[i][j] = A[i][j],vi到vj不经过任何顶点的最短路径长度
    Ak+1[i][j] = min{Ak[i][j], Ak[i][k]+Ak[k][j]}, 0<=k<=n-1
    递推过程中除了[i][j],其他元素不变可以用一个方阵进行计算,可以直接赋值修改[i][j]
    时间复杂度:O(|V|^3)
    空间复杂度:O(|V|^2)
    """
    vnum = graph.vertex_num()
    a = [[graph.get_edge(i, j) for j in range(vnum)]
            for i in range(vnum)]  # 复制一个新的邻接矩阵
    # 记录最短路径上的下一个顶点 -1 表示不经过
    # vi到vj路径上vi的后继顶点
    nvertex = [[-1 if a[i][j] == inf else j
                for j in range(vnum)]
                 for i in range(vnum)]
# [[0, -1, 2, 3, -1, -1, -1],
#  [0, 1, 2, -1, -1, 5, -1],
#  [-1, 1, 2, -1, 4, 5, -1],
#  [-1, -1, -1, 3, 4, -1, -1],
#  [-1, -1, -1, -1, 4, -1, 6],
#  [-1, -1, -1, -1, -1, 5, 6],
#  [-1, -1, -1, -1, -1, -1, 6]]
    # pprint(nvertex)
    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]  # 修改最短距离
                    nvertex[i][j] = nvertex[i][k]  # 修改最短路径上经过的顶点
    return (a, nvertex)


def get_dis_path(graph, v_start, v_end):
    """获取"""
    if v_start not in range(graph.vertex_num()) or v_end not in range(graph.vertex_num()):
        raise ValueError("超出范围")
    path = []
    a, next_vertex = all_shortest_paths(graph)
    dis = a[v_start][v_end]
    i = v_start
    while True:
        path.append(i)
        i = next_vertex[i][v_end]
        if i == -1 or i == v_end:
            path.append(i)
            break
    return dis, path


if __name__ == "__main__":
    gmat = [
        [0, inf, 5, 2, inf, inf, inf],
        [11, 0, 4, inf, inf, 4, inf],
        [inf, 3, 0, inf, 2, 7, inf],
        [inf, inf, inf, 0, 6, inf, inf],
        [inf, inf, inf, inf, 0, inf, 2],
        [inf, inf, inf, inf, inf, 0, 3],
        [inf, inf, inf, inf, inf, inf, 0],
    ]
    g = GraphAL(gmat, inf)
    for path in dijkstra_shortest_paths(g, 0):
        print(path)

#  V0到各个顶点的前一个 顶点， 距离
# (0, 0)
# (2, 8)
# (0, 5)
# (0, 2)
# (2, 7)
# (1, 12)
# (4, 9)
    paths, next_vertex = all_shortest_paths(g)
    pprint(paths)
    pprint(next_vertex)
# [[0, 8, 5, 2, 7, 12, 9],
#  [11, 0, 4, 13, 6, 4, 7],
#  [14, 3, 0, 16, 2, 7, 4],
#  [inf, inf, inf, 0, 6, inf, 8],
#  [inf, inf, inf, inf, 0, inf, 2],
#  [inf, inf, inf, inf, inf, 0, 3],
#  [inf, inf, inf, inf, inf, inf, 0]]
#
# [[0, 2, 2, 3, 2, 2, 2],
#  [0, 1, 2, 0, 2, 5, 5],
#  [1, 1, 2, 1, 4, 5, 4],
#  [-1, -1, -1, 3, 4, -1, 4],
#  [-1, -1, -1, -1, 4, -1, 6],
#  [-1, -1, -1, -1, -1, 5, 6],
#  [-1, -1, -1, -1, -1, -1, 6]]
    print(get_dis_path(g, 2, 0))
# (14, [2, 1, 0])
