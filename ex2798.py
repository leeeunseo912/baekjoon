n, m = map(int,input().split())
number = list(map(int,input().split()))

result = 0
max = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if(number[i] + number[j] + number[k] > m):
                continue
            else:
                result = number[i] + number[j] + number[k]
                if max <= result:
                    max = result

print(max)