#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 最短路径问题
@Date: 2019-10-02 09:47:54
@Author: Ulysses
@LastEditTime: 2019-10-06 14:22:13
'''
from data_structures.tree.prioqueue import PrioQueue
from data_structures.graph.graph import GraphAL, inf


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
    """任意顶点间最短路径 Floyd算法"""
    pass

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
