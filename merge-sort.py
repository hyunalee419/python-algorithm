def merge_sort(arr):
    length = len(arr)
    if length <= 1: return

    m = length//2
    L = arr[:m]
    R = arr[m:]
    merge_sort(L)
    merge_sort(R)
    
    k = i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < len(L):
        arr[k] = L[i]
        k += 1
        i += 1

    while j < len(R):
        arr[k] = R[j]
        k += 1
        j += 1

if __name__ == "__main__":
    arr = [4, 5, 3, 2, 1, 6, 8, 10, 3, 2, 1]
    print("before: ", arr)
    merge_sort(arr)
    print("after: ", arr)
