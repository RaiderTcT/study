#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-09-24 14:35:31
@Description: Depth-First Search遍历图中顶点和生成树
@LastEditTime: 2019-09-27 09:23:55
'''
from data_structures.graph.graph import GraphAL, inf
from data_structures.stack_queue.stack import SStack
from data_structures.stack_queue._quque import SQueue


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
    while not st.is_empty():  # 下次访问edges[i]
        i, edges = st.pop()
        if i < len(edges):
            vertex, _ = edges[i]
            st.push((i+1, edges))  # 下次回来访问edges[i+1]
            if not visited[vertex]:
                dfs_seq.append(vertex)
                visited[vertex] = 1
                # 先访问相邻顶点的下一个顶点
                st.push((0, graph.out_edges(vertex)))
    return dfs_seq

def dfs_graph_rec(graph, v0):
    # 使用递归
    vnum = graph.vertex_num()
    visited = [0] * vnum
    dfs_seq = []
    def dfs(graph, v):
        nonlocal visited
        nonlocal dfs_seq
        for vertex, _ in graph.out_edges(v):  # 访问顶点V
            if visited[vertex] == 0:
                visited[vertex] = 1  # 标记访问过
                dfs_seq.append(vertex)
                dfs(graph, vertex)  # 从V的邻接顶点继续深度优先搜索

    for v in range(vnum):
        if not visited[v]:  # 反复直到所有顶点都访问
            dfs(graph, v)
    return dfs_seq

def bfs_graph(graph, v0):
    vnum = graph.vertex_num()
    visited = [0] * vnum  # 记录已经访问过的顶点
    visited[v0] = 1  # 被访问过
    bfs_seq = [v0]  # bfs 遍历序列
    # yield v0
    q = SQueue()
    q.put(graph.out_edges(v0))
    while not q.is_empty():
        edges = q.get()
        for vertex, _ in edges:  # 先访问Vi所有相邻顶点Vi0, Vi1,..Vim-1
            if not visited[vertex]:
                bfs_seq.append(vertex)
                visited[vertex] = 1
                # 在依次访问Vi0，Vi1...的未访问相邻顶点
                q.put(graph.out_edges(vertex))
    return bfs_seq

# 构造DFS生成树，路径上每个顶点只需要记录它的前一个顶点信息
def dfs_span_forest(graph):
    vnum = graph.vertex_num()
    span_forest = [None] * vnum

    def dfs(graph, v):  # 使用递归 定义,记录经过的边
        nonlocal span_forest
        for u, w in graph.out_edges(v):
            if span_forest[u] is None:
                span_forest[u] = (v, w)  # 对于顶点u 需要记录的是它的前一个顶点v
                dfs(graph, u)  # 递归 搜寻从u开始的下一个顶点
    for v in range(vnum):  # G不连通时，通过循环，找到没有遍历过的顶点
        if span_forest[v] is None:
            span_forest[v] = (v, 0)  # 0代表到自身的边的长，也就是一棵树的根
            dfs(graph, v)
    return span_forest


def dfs_span_forest_nonrec(graph):
    """非递归 堆栈 DFS 生成树"""
    vnum = graph.vertex_num()
    span_forest = [None] * vnum
    st = SStack()
    st.push((0, 0, graph.out_edges(0)))  # (当前顶点，第几条出边,当前顶点的出边表)
    while not st.is_empty():
        v, i, edges = st.pop()
        if i < len(edges):
            st.push((v, i + 1, edges))  # 回来访问V的下一个邻接顶点
            u, w = edges[i][0], edges[i][1]
            if span_forest[u] is None:
                span_forest[u] = (v, w)
                # 下一次从V的邻接顶点开始深度优先搜寻
                st.push((u, 0, graph.out_edges(u)))
    return span_forest

def bfs_span_forest(graph):
    # 宽度优先
    vnum = graph.vertex_num()
    span_forest = [None] * vnum

    def bfs(gragh, v):
        nonlocal span_forest
        l = []
        for u, w in gragh.out_edges(v):
            # 先搜寻顶点v的所有相邻顶点
            if span_forest[u] is None:
                span_forest[u] = (v, w)
                l.append(u)
        for u in l:
            # 从v的相邻顶点出发继续宽度优先搜索
            bfs(graph, u)
    for v in range(vnum):
        if span_forest[v] is None:
            span_forest[v] = (v, 0)
            bfs(graph, v)
    return span_forest

def bfs_span_forest_nonrec(graph):
    vnum = graph.vertex_num()
    span_forest = [None] * vnum
    q = SQueue()
    q.put((0, graph.out_edges(0)))
    while not q.is_empty():
        v, edges = q.get()
        for u, w in edges:
            if span_forest[u] is None:
                span_forest[u] = (v, w)
                q.put((u, graph.out_edges(u)))
    return span_forest

if __name__ == "__main__":
    gmat1 = [
        [0, inf, 6, 3, 7],
        [11, 0, 4, inf, inf],
        [inf, 3, 0, inf, 5],
        [inf, inf, inf, 0, 5],
        [inf, inf, inf, inf, 0],
    ]
    g1 = GraphAL(gmat1, inf)
    print(g1.out_edges(0))
# [(0, 0), (2, 6), (3, 3), (4, 7)]

    print("深度优先，非递归 ", dfs_graph(g1, 0))
# 深度优先，非递归  [0, 2, 1, 4, 3]

    print("宽度优先 ", bfs_graph(g1, 0))
# 宽度优先  [0, 2, 3, 4, 1]

    print("深度优先，递归", dfs_graph_rec(g1, 0))
# 深度优先，递归 [0, 2, 1, 4, 3]
    print()

# 深度优先 生成树
    for i in dfs_span_forest_nonrec(g1):
        print(i)
    print()
    for i in dfs_span_forest(g1):
        print(i)
# (0, 0)  a->a
# (2, 3)  c->b
# (0, 6)  a->c
# (0, 3)  a->d
# (2, 5)  c->e
#        a
#      6/ \3
#      c   d
#    3/ \5
#    b   e
    print("-"*30)

# 宽度优先 生成树
    for i in bfs_span_forest_nonrec(g1):
        print(i)
    print()
    for i in bfs_span_forest(g1):
        print(i)
# (0, 0)  a->a
# (2, 3)  c->b
# (0, 6)  a->c
# (0, 3)  a->d
# (0, 7)  a->e
#      a
#   6/ |3 \7
#   c  d   e
# 3/
# b
