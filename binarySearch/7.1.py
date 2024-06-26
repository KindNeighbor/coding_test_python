def bSearch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array = sorted(array)
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = bSearch(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

"""
5
8 3 7 9 2
3
5 7 9
"""