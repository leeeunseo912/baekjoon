import sys
from collections import Counter

input = sys.stdin.readline

x = []
y = []

for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

# print(x)
# print(y)

cnt_x = Counter(x).most_common()
cnt_y = Counter(y).most_common()

# print(cnt_x)
# print(cnt_y)

if cnt_x[1][1] == 1:
    print(cnt_x[1][0], end=' ')
if cnt_y[1][1] == 1:
    print(cnt_y[1][0])