import math

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if dis == 0 and r1 == r2: #두원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r1-r2) == dis or r1 + r2 == dis: #내접 or 외접
        print(1)
    elif abs(r1-r2) < dis <(r1+r2): #다른 두점에서 만날 때
        print(2)
    else:
        print(0)
    