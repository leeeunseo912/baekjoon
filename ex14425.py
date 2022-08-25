import sys

input = sys.stdin.readline

n, m = map(int, input().split())

s = []
for i in range(n):
    s.append(input())

# print(s)
cnt = 0

for i in range(m):
    sentence = input()
    if sentence in s:
        cnt += 1
print(cnt)
