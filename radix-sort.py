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
    digit = len(str(max(arr)))
    
    for i in range(digit)[::-1]:
        arr_digit = [[] for i in range(10)]
        for num in arr:
            d = int(str(num)[i])
            arr_digit[d].append(num)
            
        # merge
        arr = []
        for arr_d in arr_digit:
            arr += arr_d
    return arr
    
            
if __name__ == '__main__':
    arr = [329, 457, 720, 355]
    print(arr)
    arr = radix_sort(arr)
    print(arr)
