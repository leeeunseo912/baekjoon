import sys
input = sys.stdin.readline

start = int(input())
end = int(input())

prime_num = []

for i in range(start, end+1):
    error = 0
    if i > 1:
        for j in range(2, i+1):
            if i % j == 0:
                error += 1
        if error == 1:
            prime_num.append(i)
           
# print(prime_num)

if len(prime_num) == 0:
    print(-1)
else:
    print(sum(prime_num))
    print(min(prime_num))

