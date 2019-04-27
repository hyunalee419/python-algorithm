'''
인적한 두 원소를 비교 정렬하는 알고리즘.
두 원소의 순서가 정렬되어 있지 않을 경우 두 원소를 swap한다.
1회전 수행 후 가장 큰 값이 뒤로 가므로 2회전 때는 맨 끝에 있는 자료는 정렬에서 제외한다.
- 비교회수: n-1, n-2, … , 2, 1 번 = n(n-1)/2
- 교환회수:
    - 입력 자료가 역순으로 정렬되어 있는 최악의 경우, 한 번 교환하기 위하여 3번의 이동(SWAP 함수의 작업)이 필요하므로 (비교 횟수 * 3) 번 = 3n(n-1)/2
    - 입력 자료가 이미 정렬되어 있는 최상의 경우, 자료의 이동이 발생하지 않는다.
T(n) = O(n^2)
'''

def bubble_sort(arr):
    length = len(arr)
    arr_len = range(length)
    for i in arr_len[::-1]:
        arr_sub_len = range(i)
        for j in arr_sub_len:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


if __name__ == '__main__':
    test = [1, 5, 6, 3, 1, 6, 7, 8, 3, 1, 1 ,24, 5 ,234, 32]
    print(test)
    bubble_sort(test)
    print(test)
