# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 15:37:08 2021

@author: markw''
"""

from collections import defaultdict

def makeEdges(m,n):
    edges = []
    for i in range(m):
        for j in range(n):
            if i < m - 1 : 
                edges.append([(i,j),(i+1,j)])
            if j < n - 1 : 
                edges.append([(i,j),(i,j+1)])    
    return edges

def makeNeighbours(edges, directions):
    neighbours = defaultdict(set)
    for k, [a, b] in enumerate(edges):
        if int(directions[k]):
            a, b = b, a
        neighbours[a].add(b)
    return neighbours

def existsPath(start,end,neighbours):
    visited = set([start])
    nodes = [start]
    while nodes:
        new_nodes = []
        for node in nodes:
            for neighbour in neighbours[node]:
                if neighbour == end: 
                    return True
                if (neighbour not in visited):
                    visited.add(neighbour)
                    new_nodes.append(neighbour)
        nodes = new_nodes
    return False

def solution(m,n):
    edges = makeEdges(m,n)
    feasible = []
    num_edges = len(edges)
    count = 0
    for i in range(2**num_edges):
        neighbours = makeNeighbours(edges,format(i, '0'+str(num_edges)+'b'))
        if existsPath((0,0),(m-1,n-1),neighbours):
           count += 1
           feasible.append(i)
    return count, 2**num_edges

a,b = solution(3,3)
print(a,b,a/b)
