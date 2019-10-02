#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-09-27 09:34:17
@Description: 最小生成树，Kruskal算法
@LastEditTime: 2019-10-02 09:19:05
'''
from data_structures.graph.graph import GraphAL, inf
from data_structures.tree.prioqueue import PrioQueue


def kruskal(graph):
    """
    时间复杂度： 构造edges：O(|E|);edges排序:O(nlogn);
    主循环不超过|E|次,O(|E|),进入条件体的不超过|V|-1，修改代表元需要O(|V|)，
    这部分O(|V|^2),主循环复杂度O(max(|E|, |V|^2))=O(|V|^2)
    总时间复杂度O(max(|E|log|E|, |V|^2))
    空间复杂度: O(max(|E|, |V|)) = O(|E|)
    1. 取所有顶点形成孤立的子图 T = (V, {})
    2. E中边按权值排序，每次取最短的且2顶点在不同连同分量的边加入T
    3. 重复2直至 T中所有顶点都在同一连同分量内
    """
    vnum = graph.vertex_num()
    reps = list(range(vnum))  # 连同分量的代表元
    mst, edges = [], []  # 最小生成树，所有的边
    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))  # 添加图中所有边 (边权，起始，结束)
    edges.sort()  # 按w权值排序  O(nlogn)
    for w, vi, vj in edges:
        if reps[vi] != reps[vj]:  # 边2端点要属于不同连通分量
            mst.append(((vi, vj), w))  # 添加到最小生成树序列
            if len(mst) == vnum - 1:  # 构造完成 共|V| - 1条边
                break
            rep, orep = reps[vi], reps[vj]  # 2端顶点代表元 rep - orep
            for i in range(vnum):  # 合并连同分量，统一代表元
                if reps[i] == orep:  #  rep - rep - orep
                    reps[i] = rep  # rep - rep - rep
    return mst


def prim(graph):
    """
    MST性质: G = (V, E), 令U为V的真子集,有e=(u, v)∈E,且u∈U, v∈V-U, e为所有一个
    端点在U,另一个端点在V-U中的边中权值最小.那么G中必定有一棵包括边e的最小生成树
    1. 初始(0, 0, 0)放入优先队列
    2. 将顶点0加入U,再把顶点0到其余顶点的边按权值存入优先队列
    3. 从优先队列中选择最短边,若两端分别在U和V-U就加入mst,否则丢弃
    时间复杂度: 初始化O(V), 循环内执行不超过|V|次,优先队列出入队不超过|E|次, O(|E|log|E|)
    空间复杂度: mst表和优先队列O(|V|)和O(|E|), 总复杂度O(|E|)
    """
    vnum = graph.vertex_num()
    mst = [None] * vnum
    # 候选边(w, vi, vj)
    cands = PrioQueue([(0, 0, 0)])  # 初始顶点0到自身, 边长为0
    count = 0
    while count < vnum and not cands.is_empty():
        w, u, v = cands.dequeue()  # 取当前最短边
        if mst[v]:
            continue  # 顶点v已在T内 寻找其他边
        mst[v] = ((u, v), w)  # 记录新的mst边和顶点
        count += 1
        for vi, w in graph.out_edges(v):  # 考虑v的邻接顶点构成的边
            if not mst[vi]:  # 不在mst的是候选边, (u, v)加入mst时,排除v的
                # 邻接边 (v, u)
                cands.enqueue((w, v, vi))
    return mst


if __name__ == "__main__":
    gmat = [
        [0, 5, 11, 5, inf, inf, inf],
        [5, 0, inf, 3, 9, inf, 7],
        [11, inf, 0, 7, inf, 6, inf],
        [5, 3, 7, 0, inf, inf, 20],
        [inf, 9, inf, inf, 0, inf, 8],
        [inf, inf, 6, inf, inf, 0, 8],
        [inf, 7, inf, inf, 8, 8, 0],
    ]
    g = GraphAL(gmat, inf)
    print([[g.get_edge(0, v), v, 0]for v in range(g.vertex_num())])
    mst = kruskal(g)
    for item in mst:
        print(item)
    print("=" * 30)
    mst = prim(g)
    for item in mst:
        print(item)
