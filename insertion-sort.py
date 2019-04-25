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
