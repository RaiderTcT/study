#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data_structures.graph.graph import *
'''
@Author: Ulysses
@Date: 2019-10-12 14:43:03
@Description: 有向图 AOV, 拓扑
@LastEditTime: 2019-10-14 14:43:37
'''
"""
有向图的应用: 顶点表示工程里的不同活动, 边表示各项活动之间的先后顺序关系
这样的有向图称为AOV(activity on vertext network)
拓扑序列: AOV网N中所有顶点排除一个序列
S = vi0, vi1, ..., vin-1  满足: N中存在顶点vi到vj的路径, 那么S里vi就拍照vj之前
S称为N的拓扑序列, 构造的过程称为拓扑排序
无任何回路的AOV网都可以做出拓扑序列
"""

def topo_sort(graph):
    """
    有向图拓扑排序
    1. 选出入度为0的顶点加入序列
    2. 删除图中所选顶点及其所有边
    3. 重复1和2 直至所有顶点都选出或没有入度非0的顶点
    时间复杂度 O(|V|+|E|)
    空间复杂度 O(|V|)
    """
    vnum = graph.vertex_num()
    # 在indegree里维持一个 0度表, 记录已知的所有入度为0但没有处理的顶点
    indegree, topo_seq = [0] * vnum, []
    # 记录zerov第一个入度为0的顶点下标, indegree[zerov]记录下一个入度为0的顶点下标
    # 依次类推, 若最后一个顶点下标为v, indegree[v]中存入-1
    zerov = -1
    # 建立初始的入度表
    for vi in range(vnum):
        for v, _ in graph.out_edges(vi):
            indegree[v] += 1
    # 在入度表中建立 0度表, 相当于一个顶点栈, zerov为栈顶,-1表示栈结束
    for vi in range(vnum):
        if indegree[vi] == 0:
            # 把当时的zerov值存入indegree[vi],把v存入zerov.相当于v入栈
            indegree[vi] = zerov
            zerov = vi
    for _ in range(vnum):
        if zerov == -1:  # 没有拓扑序列
            return False
        # 把入度为0的顶点加入拓扑序列
        topo_seq.append(zerov)
        # 相当于从0度表中弹出元素
        vi = zerov
        # 下一个入度为0,还没处理的顶点
        zerov = indegree[zerov]
        # vi检查出边
        for v, _ in graph.out_edges(vi):
            # 删除vi和出边 对应的邻接顶点v的入度减一
            indegree[v] -= 1
            if indegree[v] == 0:
                # v入度为0 加入0度表
                indegree[v] = zerov
                zerov = v
    return topo_seq

# AOE网络的关键路径  critical path
def event_earliest_time(vnum, graph, toposeq):
    """
    事件的最早发生时间: 前提活动都要完成
    ee[0] = 0; ee[j] = max{ee[i] + w(<vi, vj>)|<vi, vj>∈E}, 1<=j<=n-1
    """
    ee = [0] * vnum
    for i in toposeq:
        for j, w in graph.out_edges(i):
            if ee[i] + w > ee[j]:
                ee[j] = ee[i] + w  # vj要在其所有入边活动完成后开始
    return ee

def event_lastest_time(vnum, graph, toposeq, eelast):
    """
    事件的最迟发生时间:在后一个事件发生前,完成本事件
    le[n-1] = ee[n-1]; le[i] = min{le[j]-w(<vi, vj>)|<vi, vj>∈E}, 0<=i<=n-2
    """
    le = [eelast]*vnum  # 最后一个事件的最迟发生时间=最早发生时间
    for k in range(vnum-2, -1, -1):  # 需要逆拓扑序列顺序进行
        i = toposeq[k]
        for j, w in graph.out_edges(i):
            if le[j] - w < le[i]:
                le[i] = le[j] - w
    return le

def critical_paths(graph):
    """
    时间复杂度: 检查每个顶点和每个顶点边表中所有边 O(|V|+||E)
    空间复杂度: O(|E|)
    """
    def event_earliest_time(vnum, graph, toposeq):
        """
        事件的最早发生时间: 前提活动都要完成
        ee[0] = 0; ee[j] = max{ee[i] + w(<vi, vj>)|<vi, vj>∈E}, 1<=j<=n-1
        """
        ee = [0] * vnum
        for i in toposeq:
            for j, w in graph.out_edges(i):
                if ee[i] + w > ee[j]:
                    ee[j] = ee[i] + w  # vj要在其所有入边活动完成后开始
        return ee

    def event_lastest_time(vnum, graph, toposeq, eelast):
        """
        事件的最迟发生时间:在后一个事件发生前,完成本事件
        le[n-1] = ee[n-1]; le[i] = min{le[j]-w(<vi, vj>)|<vi, vj>∈E}, 0<=i<=n-2
        """
        le = [eelast]*vnum  # 最后一个事件的最迟发生时间=最早发生时间
        for k in range(vnum-2, -1, -1):  # 需要逆拓扑序列顺序进行
            i = toposeq[k]
            for j, w in graph.out_edges(i):
                if le[j] - w < le[i]:
                    le[i] = le[j] - w
        return le

    def crt_paths(vnum, graph, ee, le):
        crt_actions = []
        for i in range(vnum):
            for j, w in graph.out_edges(i):
                if ee[i] == le[j] - w:  # 关键活动
                    # (i,j,t)顶点i到j的事件需要在t时间开始
                    crt_actions.append((i, j, ee[i]))
        return crt_actions

    toposeq = topo_sort(graph)
    if not toposeq:
        return False
    vnum = graph.vertex_num()
    ee = event_earliest_time(vnum, graph, toposeq)
    le = event_lastest_time(vnum, graph, toposeq, ee[vnum-1])
    return crt_paths(vnum, graph, ee, le)


if __name__ == '__main__':
    gmat = [
       # 1  2  3  4  5  6  7  8  9  10
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    # 事件自身到自身没有 活动
    gmat1 = [
       # 0    1    2    3   4    5    6    7    8
        [inf,   7,  13,   8, inf, inf, inf, inf, inf],
        [inf, inf,  4,  inf, inf,  14, inf, inf, inf],
        [inf, inf, inf,  inf,  5, inf,  8,  12,  inf],
        [inf, inf, inf, inf,  13, inf, inf, 10,  inf],
        [inf, inf, inf, inf, inf,  7,   3,  inf, inf],
        [inf, inf, inf, inf, inf, inf, inf, inf,   5],
        [inf, inf, inf, inf, inf, inf, inf, inf,   7],
        [inf, inf, inf, inf, inf, inf, inf, inf,   8],
        [inf, inf, inf, inf, inf, inf, inf, inf, inf],
    ]
    g = GraphAL(gmat, un_conn=0)
    # print(topo_sort(g))
    # [1, 0, 4, 3, 2, 6, 5, 7, 9, 8]
    g1 = GraphAL(gmat1, un_conn=inf)
    print(topo_sort(g1))
    print(critical_paths(g1))
    # [(0, 2, 0), (0, 3, 0), (2, 7, 13), (3, 4, 8), (4, 5, 21), (5, 8, 28), (7, 8, 25)]

    ee = event_earliest_time(g1.vertex_num(), g1, topo_sort(g1))
    le = event_lastest_time(g1.vertex_num(), g1, topo_sort(g1), ee[-1])
    # 每个顶点所代表的事件最早开始时间和最迟开始时间
    print(list(zip(ee, le)))
    # [(0, 0), (7, 9), (13, 13), (8, 8), (21, 21), (28, 28), (24, 26), (25, 25), (33, 33)]
