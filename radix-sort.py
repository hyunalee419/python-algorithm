'''
n개의 d자리 정수들
가장 낮은 자리수부터 정렬 (stable을 유지해야한다.)
stabe: i, k (i < k) 인덱스의 값이 동일할 때 정렬한 후에도 i < k를 유지해야 함.
329     720     720     329
457  => 355  => 329  => 355
720     457     355     457
355     329     457     720
'''
def radix_sort(arr):
    arr_digit = range(len(arr[0]))
    queue = []
    for d_idx in arr_digit[::-1]:
        for num in arr:
            d = int(str(num)[d_idx])
            if not queue[d]:
                queue[d] = []
            queue[d].append(num)
        
        arr = []
        for i in range(queue):
            arr = arr + queue[i]
            
if __name__ == '__main__':
    arr = [329, 457, 720, 355]
    print(arr)
    radix_sort(arr)
    print(arr)
