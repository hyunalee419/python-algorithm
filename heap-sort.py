'''
heap: 한 노드(node)가 최대 두 개의 자식노드(child node)를 가지면서,
마지막 레벨을 제외한 모든 레벨에서 노드들이 꽉 채워진 완전 이진 트리(complete binary tree)를 만족해야 한다.
- heapify: 주어진 자료구조에서 힙 성질을 만족하도록 하는 연산. 
- max heap(최대 힙): 자식 노드의 값보다 부모 노드의 값이 '큰' 힙 구조.
- min heap(최소 힙): 자식 노드의 값보다 부모 노드의 값이 '작은' 힙 구조.
heap sort는 최대 힙 또는 최소 힙을 만족하며 정렬하는 방식. 어레이의 각 인덱스는 root 노드부터 차례대로 각 노드로 생각하면 된다.
예, arr = [5, 4, 3, 2, 1, 6, 3, 1, 10, 4]
            5[0]
       4[1]      3[2]
    1[3]  6[4] 3[5]  1[6]
 10[7] 4[8]
1. max heap(최대 힙)을 만든다.
2. root 노드의 값을 가장 마지막 index의 값과 swap한다.
3. 1,2방식을 반복한다. (대신, 이때 부터는 root 노드와 swap한 마지막 index를 제외하고 정렬한다.)
O(NlogN): 정렬하는데 트리구조 이기때문에 logN * heapify 방식을 만드는데 N = N * logN = O(NlogN)
'''
def heapify(arr):
    length_arr = len(arr)
    if length_arr <= 1:
        return arr
    
    last_idx = length_arr - 1
    if last_idx % 2 == 1:
        parent_idx = (last_idx - 1)//2
        if arr[parent_idx] < arr[last_idx]:
            arr[parent_idx], arr[last_idx] = arr[last_idx], arr[parent_idx]
        last_idx -= 1

    for i in range(last_idx, 0, -2):
        max_idx = i
        if arr[max_idx] < arr[i - 1]:
            max_idx = i - 1
            
        parent_idx = (i - 2)//2
        if arr[parent_idx] < arr[max_idx]:
            arr[parent_idx], arr[max_idx] = arr[max_idx], arr[parent_idx] 
    return arr

def heap_sort(arr):
    length_arr = len(arr)
    arr_max_heap = arr
    for i in range(length_arr, 1, -1):
        arr_max_heap = heapify(arr_max_heap[:i])
        arr[i - 1] = arr_max_heap[0]
        arr_max_heap[0], arr_max_heap[i - 1] = arr_max_heap[i - 1], arr_max_heap[0]

    return arr

if __name__ == '__main__':
    arr = [1, 5, 2, 4, 23, 15, 1, 8, 9, 10]
    print(arr)
    arr = heap_sort(arr)
    print(arr)
