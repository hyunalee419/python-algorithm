"""
Breadth First Search
---
너비 우선 탐색
- 큐를 이용해 구현
- 형제 노드를 출력한 후 자식 노드를 출력
graph = {'A': ['B', 'C', 'D'],
         'B': ['A', 'E', 'F'],
         'C': ['A', 'G'],
         'D': ['A', 'H', 'I'],
         'E': ['B'],
         'F': ['B', 'J'],
         'G': ['C'],
         'H': ['D'],
         'I': ['D', 'K', 'L'],
         'J': ['F'],
         'K': ['I'],
         'L': ['I']}

출력: A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> K -> L
"""

def bfs(graph, root):
    queue = graph[root]
    visited = [root]

    while queue:
        node = queue.pop(0)
        children = list(set(graph[node]) - set(visited) - set(queue))
        queue = queue + children
        visited.append(node)
    print(visited)

if __name__ == '__main__':
    graph = {'A': ['B', 'C', 'D'],
         'B': ['A', 'E', 'F'],
         'C': ['A', 'G'],
         'D': ['A', 'H', 'I'],
         'E': ['B'],
         'F': ['B', 'J'],
         'G': ['C'],
         'H': ['D'],
         'I': ['D', 'K', 'L'],
         'J': ['F'],
         'K': ['I'],
         'L': ['I']}
    bfs(graph, 'A')
