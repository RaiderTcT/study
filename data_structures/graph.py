#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-09-24 09:01:00
@Description: 图的基本实现
@LastEditTime: 2019-09-24 14:09:24
'''
from collections import defaultdict

class GraphError(TypeError):
    pass

inf = float("inf")  # 无穷大，表示无


# 邻接矩阵表示
class Graph:
    def __init__(self, mat, un_conn=0):
        """
        构造图
        Args:
            mat (list): 邻接矩阵，嵌套list形式
            un_conn (int, optional): 参数为无关联特殊值. Defaults to 0.

        Raises:
            ValueError: 矩阵不是方阵
        """
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("mat需要为方阵")
        self._mat = [mat[i][:] for i in range(vnum)]  # 拷贝生成新的矩阵
        self._vnum = vnum  # 顶点数目
        self._unconn = un_conn
        self._edges = defaultdict(list)

    def vertex_num(self):
        return self._vnum

    def _invalid(self, v):
        # 检查顶点下标是否非法
        return 0 > v or v >= self._vnum

    def add_vertex(self):
        raise GraphError('不支持的操作')

    def add_edge(self, vi, vj, val=1):
        """添加vi到vj的边"""
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(f"顶点{vi} 或者 {vj}为不合法的顶点")
        self._mat[vi][vj] = val
        self._edges[vi] = self._out_edges(self._mat[vi], self._unconn)

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(f"顶点{vi} 或者 {vj}为不合法的顶点")
        return self._mat[vi][vj]

    def out_edges(self, vi):
        """获取顶点vi的出边表"""
        if self._invalid(vi):
            raise GraphError(f"顶点{vi}为不合法的顶点")
        if vi not in self._edges:
            self._edges[vi] = self._out_edges(self._mat[vi], self._unconn)
        return self._edges[vi]

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))  # 出边 终点顶点，边的信息（权值）
        return edges

    def __str__(self):
        return f"[\n" + ',\n'.join(map(str, self._mat)) + "\n]"\
            + "\nUnconnected: " + str(self._unconn)


# 邻接表表示
class GraphAL(Graph):
    def __init__(self, mat=[], un_conn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("mat需要为方阵")
        # [每个顶点的出边表]
        self._mat = [
            Graph._out_edges(mat[i], un_conn) for i in range(vnum)
        ]
        self._vnum = vnum
        self._unconn = un_conn

    def add_vertex(self):
        self._mat.append([])
        num = self._vnum
        self._vnum += 1
        return num

    def add_edge(self, vi, vj, val=1):
        # val为0 表示删去这条边
        if self._vnum == 0:
            raise GraphError("图为空")
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(f"顶点{vi} 或者 {vj}为不合法的顶点")
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:  # 找到终止顶点
                self._mat[vi][i] = (vj, val)  # 删除
                if val == self._unconn:
                    self._mat[vi].pop(i)
                return
            if row[i][0] > vj:
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))  # 添加边

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(f"顶点{vi} 或者 {vj}为不合法的顶点")
        for i, val in self._mat(vi):
            if i == vj:
                return val
        return self._unconn

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(f"不合法的顶点 {vi}")
        return self._mat[vi]

# dict 形式表示
class GraphDict(Graph):
    def __init__(self, mat, un_conn=0):
        self._vnum = len(mat)
        self._unconn = un_conn
        self._mat = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] != un_conn:
                    self._mat[(i, j)] = mat[i][j]

    def add_vertex(self):
        num = self._vnum
        self._vnum += 1
        self._mat.update({(num, num): 0})  # 添加到自身的边
        return num

    def add_edge(self, vi, vj, val=1):
        # val为0 表示删去这条边
        if self._vnum == 0:
            raise GraphError("图为空")
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(f"顶点{vi} 或者 {vj}为不合法的顶点")
        key = (vi, vj)
        if key in self._mat:
            if val == self._unconn:
                self._mat.pop(key)
        else:
            self._mat[key] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(f"顶点{vi} 或者 {vj}为不合法的顶点")
        return self._mat.get((vi, vj), None)

    def out_edges(self, vi):
        if self._invalid(vi) :
            raise GraphError(f"顶点{vi}为不合法的顶点")
        l = []
        for key, val in self._mat.items():
            if key[0] == vi:
                l.append((key[1], val))
        return l

    def __str__(self):
        return f"[\n" + ',\n'.join(map(str, self._mat.items())) + "\n]"\
            + "\nUnconnected: " + str(self._unconn)

if __name__ == '__main__':
    gmat1 = [
        [0, 0, 1],
        [1, 0, 1],
        [0, 1, 0]
    ]
    gmat2 = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ]
    # 带权值
    gmat3 = [
        [0, inf, 6, 3, inf],
        [11, 0, 4, inf, inf],
        [inf, 3, 0, inf, 5],
        [inf, inf, inf, 0, 5],
        [inf, inf, inf, inf, 0],
    ]
    g1 = Graph(gmat1)
    g2 = Graph(gmat2)
    g3 = Graph(gmat3, inf)
    print(g1)
# [
# [0, 0, 1],
# [1, 0, 1],
# [0, 1, 0]
# ]
# Unconnected: 0
    print("-"*30)
    print(g2)
# [
# [0, 1, 1, 0],
# [1, 0, 1, 0],
# [1, 1, 0, 1],
# [0, 0, 1, 0]
# ]
# Unconnected: 0
    for edge in g2.out_edges(0):  # a点 出表
        print(edge)
# (1, 1)
# (2, 1)
    g2.add_edge(0, 3, 1)  # 添加a到d的边
    print()
    for edge in g2.out_edges(0):  # a点 出表
        print(edge)
# (1, 1)
# (2, 1)
# (3, 1)
    print("-"*30)
    for edge in g3.out_edges(2):  # c 出表
        print(edge)
# (1, 3)
# (2, 0)
# (4, 5)
    print("-"*30)
    gal3 = GraphAL(gmat3, inf)
    print(gal3)
# [
# [(0, 0), (2, 6), (3, 3)],
# [(0, 11), (1, 0), (2, 4)],
# [(1, 3), (2, 0), (4, 5)],
# [(3, 0), (4, 5)],
# [(4, 0)]
# ]
    gal3.add_edge(0, 2, inf)  # 删去 a -> c
    print(gal3)
# [
# [(0, 0), (3, 3)],
# [(0, 11), (1, 0), (2, 4)],
# [(1, 3), (2, 0), (4, 5)],
# [(3, 0), (4, 5)],
# [(4, 0)]
# ]
    gal3.add_edge(0, 4, 3)  # 添加 a -> e
    print(gal3)
# [
# [(0, 0), (3, 3), (4, 3)],
# [(0, 11), (1, 0), (2, 4)],
# [(1, 3), (2, 0), (4, 5)],
# [(3, 0), (4, 5)],
# [(4, 0)]
# ]
    gal3.add_vertex()  # 添加顶点f
    gal3.add_edge(1, 5, 3)  # b -> f
    gal3.add_edge(5, 2, 7)  # f -> c
    gal3.add_edge(5, 4, 10)  # f -> e
    print(gal3.out_edges(1))
    print(gal3.out_edges(5))
# [(0, 11), (1, 0), (2, 4), (5, 3)]
# [(2, 7), (4, 10)]

    print("-"*30)
    g3_dict = GraphDict(gmat3, inf)
    print(g3_dict)
# [
# ((0, 0), 0),
# ((0, 2), 6),
# ((0, 3), 3),
# ((1, 0), 11),
# ((1, 1), 0),
# ((1, 2), 4),
# ((2, 1), 3),
# ((2, 2), 0),
# ((2, 4), 5),
# ((3, 3), 0),
# ((3, 4), 5),
# ((4, 4), 0)
# ]
    print(g3_dict.out_edges(2))  # c出表
# [(1, 3), (2, 0), (4, 5)]
    g3_dict.add_vertex()
    g3_dict.add_edge(5, 2, 3)
    g3_dict.add_edge(5, 4, 7)
    print(g3_dict.out_edges(5))
# [(5, 0), (2, 3), (4, 7)]
