#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-09-24 14:35:31
@Description: Depth-First Search遍历图中顶点和生成树
@LastEditTime: 2019-09-24 19:24:12
'''
from data_structures.graph.graph import GraphAL, inf
from data_structures.stack_queue.stack import SStack
from data_structures.stack_queue._queue import SQueue


# 复杂度分析构造visited 和 dfs_seq表，时间复杂度O(|V|)
# 出栈入栈次数取决与边的数目，总开销O(|E|)， 构造out_edges O(|V|*|V|)
# |E| <= |V|*|V|，总复杂度O(max(|V|, |E|))
# 空间复杂度 O(|V|)
def dfs_graph(graph, v0):
    # 遍历从v0出发能访问的所有顶点
    vnum = graph.vertex_num()
    visited = [0] * vnum  # 记录已经访问过的顶点
    visited[v0] = 1  # 被访问过
    dfs_seq = [v0]  # dfs 遍历序列
    st = SStack()
    # (便表下标, 边表)
    st.push((0, graph.out_edges(v0)))  # 从v0出发 访问下一个顶点
    while not st.is_empty():
        i, edges = st.pop()
        if i < len(edges):
            vertex, _ = edges[i]
            st.push((i + 1, edges))  # 下一个 当前顶点 能够访问的顶点
            if not visited[vertex]:
                dfs_seq.append(vertex)
                visited[vertex] = 1
                st.push((0, graph.out_edges(vertex)))  # 下一个顶点 能访问的顶点
    return dfs_seq


def bfs_graph(graph, v0):
    vnum = graph.vertex_num()
    visited = [0] * vnum  # 记录已经访问过的顶点
    visited[v0] = 1  # 被访问过
    bfs_seq = [v0]  # dfs 遍历序列
    yield v0
    q = SQueue()
    q.put((0, graph.out_edges(v0)))
    while not q.is_empty():
        i, edges = q.get()
        if i < len(edges):
            vertex, _ = edges[i]
            q.put((i + 1, edges))
            if not visited[vertex]:
                visited[vertex] = 1
                yield vertex
                # bfs_seq.append(vertex)
                q.put((0, graph.out_edges(vertex)))
    # return bfs_seq


# 构造DFS生成树，路径上每个顶点只需要记录它的前移一个顶点信息
def dfs_span_forest(graph):
    pass


if __name__ == "__main__":
    gmat1 = [
        [0, inf, 6, 3, inf],
        [11, 0, 4, inf, inf],
        [inf, 3, 0, inf, 5],
        [inf, inf, inf, 0, 5],
        [inf, inf, inf, inf, 0],
    ]
    g1 = GraphAL(gmat1, inf)

    print(dfs_graph(g1, 0))
    for i in bfs_graph(g1, 0):
        print(i)
