import sys
input = sys.stdin.readline

n, m = map(int,input().split())

num = list(map(int, input().split()))

temp = 0
pre_sum = [0]

for i in num:
    temp += i
    pre_sum.append(temp)

for i in range(m):
    start, end = map(int, input().split())
    print(pre_sum[end] - pre_sum[start-1])


