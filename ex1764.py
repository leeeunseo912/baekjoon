import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))
hear = set()

for i in range(n):
    name = input()
    hear.add(name)

result = []

for i in range(m):
    name = input()
    if name in hear:
        result.append(name)
       

print(len(result))
result.sort()
for i in result:
    print(i, end="")

