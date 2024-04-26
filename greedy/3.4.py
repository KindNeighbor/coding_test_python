N, K = map(int, input().split())

idx = 0
while True:
    if N == 1:
        break
    if N % K == 0:
        N /= K
        idx += 1
    else:
        N -= 1
        idx += 1

print(idx)

'''
25 5
'''