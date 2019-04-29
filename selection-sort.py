'''
1. 주어진 배열에서 최솟값을 찾아 맨 앞에 위치한 값과 SWAP한다.
2. 다음 수행시에 처음 위치의 값을 제외한 나머지 값들을 1번을 수행한다.
장점: 자료 이동 횟수가 미리 결정된다.
단점: 값이 같은 레코드가 있는 경우 상대적인 위치가 변경될 수 있다.
- 비교회수:
    - 외부 루프: (n-1)번
    - 내부 루프: n-1, n-2, ..., 2, 1번
- 교환회수:
    - 외부 루프의 실행 횟수와 동일
    - SWAP을 위해 3번의 이동이 필요
T(n) = O(n^2)
'''
def selection_sort(arr):
    arr_len = range(len(arr))
    for i in arr_len:
        min_idx = i
        arr_sub_len = range(i, len(arr))
        for j in arr_sub_len:
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


if __name__ == '__main__':
    test = [3, 4, 1, 2, 1, 2, 3, 5, 6, 7 ,4, 23423, 123, 334, 22]
    print(test)
    selection_sort(test)
    print(test)
