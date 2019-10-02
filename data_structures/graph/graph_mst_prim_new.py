#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 改进Prim算法,降低空间需求
@Date: 2019-10-01 14:25:20
@Author: Ulysses
@LastEditTime: 2019-10-02 09:02:40
'''
from data_structures.tree.prioqueue import PrioQueue
from data_structures.graph.graph import GraphAL, inf


class DecPrioHeap(PrioQueue):
    """减权堆"""
    def __init__(self, elist):
        self._elems = list(elist)
        self._elems_1 = [None]*len(elist)
        if elist:
            self.buildheap()
            for i in range(len(self._elems)):
                self._elems_1[self._elems[i][1]] =  self._elems[i]

    def getmin(self):
        e = self.dequeue()
        return e

    def weight(self, ind):
        return self._elems_1[ind][0]

    def dec_weight(self, ind, w, other):
        e = self._elems_1[ind]
        self._elems.remove(e)
        e = [w, ind, other]
        # self._elems[i] = [w, ind, other]
        # e = self._elems[i]
        self._elems_1[ind] = e
        self._elems.append(None)
        self.siftup(e, len(self._elems)-1)


def prim(graph):
    """
    空间复杂度O(|V|), 时间复杂度O(max(|V|log|V|, |E|log|V|))
    """
    vnum = graph.vertex_num()
    wv_seq = [[graph.get_edge(0, v), v, 0] for v in range(vnum)]
    connects = DecPrioHeap(wv_seq)    # record vertices
    mst = [None]*vnum
    while not connects.is_empty():
        w, mv, u = connects.getmin()  # take nearest vertex and edge
        if w == inf:
            break
        mst[mv] = ((u, mv), w)  # new MST edge and vertex vmin
        for v, w in graph.out_edges(mv):  # edge is in form (v, w)
            if not mst[v] and w < connects.weight(v):
                connects.dec_weight(v, w, mv)
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
    mst = prim(g)
    for item in mst:
        print(item)
