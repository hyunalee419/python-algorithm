# Tree의 종류
## Tree
부모 자식 관계를 자료구조. 
leaf: 트리의 가장 끝에 자식이 없는 노드

## Binary Tree (이진 트리)
자식 노드가 두개 이하인 트리

## Binary Search Tree (이진 검색 트리)
이진 트리이면서, 왼쪽 노드의 데이터와 그 이하 노드들이 현재 노드의 값보다 작고 오른쪽 노드의 데이터와 그 이하 노드의 데이터가 현재 노드의 데이터보다 커야한다.
트리에서 값을 찾고자 할 때 해당 노드보다 (찾고자 하는 데이터가) 크면 오른쪽으로 보고 작으면 왼쪽으로 본다.

## Balance
한 쪽으로 치우치지 않은 트리.
왼쪽 오른쪽 노드의 개수가 정확하게 일치하지 않아도 된다.
### 밸런스 트리의 종류
- red-black tree
- AVL tree

## Complete Binary Tree (완전 이진 트리)
바이너리 트리의 leaf 노드들이 비어있을 때 왼쪽부터 채워진 트리

## Full Binary Tree
차일드를 갖지 않거나 모두 가진 트리

**주의** : 한국어 교재에 포화 이진 트리라고 되어있지만 설명은 Perfect Binary Tree에 대해 설명하고 있는 교재가 있다. 외국 교재의 설명과 다르니 주의.

## Perfect Binary Tree
자식노드가 완벽하게 두개를 다 갖고 있는 트리
레벨의 개수를 n이라고 가정할 때 2^(n-1)의 노드를 가진 트리 

# Binary Tree의 3가지 순회방법
예제 트리:
     (1)
  (2)   (3)
(4) (5)

## Inorder
Left - Root - Right: 4 - 2 - 5 - 1 - 3

## Preorder
Root - Left - Right: 1 - 2 - 4 - 5 - 3

## Postorder
Left - Right - Root: 4 - 5 - 2 - 3 - 1

---
**참조**
- [자료구조 알고리즘: Tree의 종류](https://www.youtube.com/watch?v=LnxEBW29DOw)
- [Binary Tree의 3가지 순회방법](https://www.youtube.com/watch?v=QN1rZYX6QaA)
