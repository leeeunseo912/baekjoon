import sys

input = sys.stdin.readline

num = int(input())
width = []
height = []
total = []

for i in range(6):
    dir, len = map(int, input().split(' '))
    if dir == 1 or dir == 2:
        width.append(len)
        total.append(len)
    else:
        height.append(len)
        total.append(len)

print(total)
big_area = (max(width)*max(height))

maxhidx = total.index(max(height))
maxwidx = total.index(max(width))
print(maxhidx, maxwidx)
small1 = abs(total[maxhidx-1] - total[(maxhidx-5 if maxhidx == 5 else maxhidx +1)])
small2 = abs(total[maxwidx-1] - total[(maxwidx-5 if maxwidx == 5 else maxwidx +1)])
print(small1, small2)

area = big_area - (small1 * small2)
print(area * num)
