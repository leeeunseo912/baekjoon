import sys
import math
input = sys.stdin.readline

n = int(input())

num = []
for i in range(n):
    num.append(int(input()))
print("원래입력값", num)
num.sort()
print("정렬된", num)
print(round(sum(num)/n))
print(num[math.ceil(n/2)-1])

print(max(num)-min(num))