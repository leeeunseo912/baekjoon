import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
card = deque([])

for i in range(1,n+1,1):
    card.append(i)

for i in range(n-1):
    card.popleft()
    # print("맨앞에꺼 없애기 == ", card)
    card.append(card[0])
    card.popleft()
    # print("맨앞에꺼 맨뒤로 옮기기 == ", card)
print(card[0])