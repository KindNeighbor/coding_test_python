n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()

for i in array:
    print(i, end=' ')

"""
3
15
27
12
"""