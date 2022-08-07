import sys
import math
from collections import Counter

input = sys.stdin.readline

n = int(input())

num = []
for i in range(n):
    num.append(int(input()))
# print("원래입력값", num)
num.sort()
# print("정렬된", num)

#산술평균
print(round(sum(num)/n))

#중앙값
print(num[math.ceil(n/2)-1])

#최빈값
cnt = Counter(num).most_common(2)

if len(num) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

#범위
print(max(num)-min(num))