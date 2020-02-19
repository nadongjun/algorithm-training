# -*- coding: utf-8 -*- 
from __future__ import print_function

N, M, V = map(int, raw_input().split())

graph_list = [set([]) for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, raw_input().split())
    graph_list[i].add(j)
    graph_list[j].add(i)

def dfs(graph_list, start):
    visited = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack += sorted(list(graph_list[node] - set(visited)), reverse = True)
            
    return visited

def bfs(graph_list, start):
    visited = []
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue += sorted(list(graph_list[node] - set(visited)))

    return visited


for i in list(dfs(graph_list, V)):
    print(i, end=" ")

print()

for j in list(bfs(graph_list, V)) :
    print(j, end=" ")
    
#Python 2.7.10
#https://this-programmer.com/entry/%EB%B0%B1%EC%A4%801260%ED%8C%8C%EC%9D%B4%EC%8D%AC-DFS%EC%99%80-BFS
