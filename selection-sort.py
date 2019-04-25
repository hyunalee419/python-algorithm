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
