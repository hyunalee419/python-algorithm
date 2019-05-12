'''
1. pivot(임의의 값)을 정한다.
2. pivot을 기준으로 pivot보다 작은 값은 왼쪽, 큰 값은 오른쪽으로 나눈다. (2개의 리스트로 나눈다.)
3. 리스트의 길이가 0 또는 1개로 나누어질 때까지 1,2의 과정을 반복한다.
4. 분할된 리스트를 하나의 리스트로 합친다.
복잡도: 나누는데 logN, 정렬하는데 n = O(NlogN)
최악의 경우: 분리가 한쪽으로 몰리는 경우 logN이 아닌 N이 걸리기때문에, O(n^2)
'''
def quick_sort(arr):
    m = len(arr)
    if m <= 1: return
    
    # divide & conquer
    pivot = arr[m//2]
    L = []
    R = []
    for n in arr:
        if n <= pivot:
            L.append(n)
        else:
            R.append(n)
    quick_sort(L)
    quick_sort(R)
    
    # merge
    arr = L + R
    
if __name__ == '__main__':
    arr = [4, 2, 3,5 ,1 2, 5, 2, 12]
    print(arr)
    quick_sort(arr)
    print(arr)
