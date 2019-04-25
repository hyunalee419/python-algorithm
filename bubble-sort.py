def bubble_sort(arr):
    length = len(arr)
    arr_len = range(length)
    for i in arr_len:
        arr_sub_len = range(i + 1, length)
        for j in arr_sub_len:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


if __name__ == '__main__':
    test = [1, 5, 6, 3, 1, 6, 7, 8, 3, 1, 1 ,24, 5 ,234, 32]
    print(test)
    bubble_sort(test)
    print(test)
