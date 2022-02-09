def  solve(a):
    total=0
    for i in a:
        total += i
    return total

a = list(map(int,input().split()))
print(solve(a))