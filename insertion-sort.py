'''
i번째 인덱스의 값을 0부터 i-1번째의 값들중 자신의 위치를 찾아 정렬을 완성하는 알고리즘
처음 key값을 "두번째 값"부터 시작한다.
최선의 경우: O(n)
- 비교 횟수: 이동없이 한번의 비교만 이루어진다.
- 외부 루프: (n-1)번
최악의 경우: O(n^2)
- 비교 횟수: 외부 루프 안의 각 반복마다 i번의 비교 수행
- 교환 횟수: 외부 루프의 각 단계마다 (i+2)번의 이동 발생
'''
def insertion_sort(arr):
    arr_len = range(1, len(arr))
    for i in arr_len:
        arr_sort_len = range(i)
        for j in arr_sort_len:
            if arr[i] < arr[j]:
                pop_num = arr.pop(i)
                arr.insert(j, pop_num)
                break
    return arr


if __name__ == '__main__':
    test = [3, 2, 1, 2, 4, 1, 21, 534, 123,3, 53, 10]
    print(test)
    insertion_sort(test)
    print(test)
