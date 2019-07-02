"""
Depth First Search
---
깊이 우선 탐색
- 스택을 이용해 구현
- 재귀호출을 이용해 구현
- 자식 노드의 값부터 출력 후 형제 노드 출력

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
         
출력: A -> B -> E -> F -> J -> C -> G -> D -> H -> I -> K -> L
"""

def dfs(graph, root):
    stack = graph[root]
    visited = [root]

    while stack:
        node = stack.pop()
        children = list(set(graph[node]) - set(visited) - set(stack))
        stack = stack + children
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
    dfs(graph, 'A')
