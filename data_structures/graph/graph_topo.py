#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data_structures.graph.graph import *
'''
@Author: Ulysses
@Date: 2019-10-12 14:43:03
@Description: 有向图 AOV, 拓扑
@LastEditTime: 2019-10-12 17:12:31
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
    g = GraphAL(gmat, un_conn=0)
    print(topo_sort(g))
    # [1, 0, 4, 3, 2, 6, 5, 7, 9, 8]
