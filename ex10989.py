import sys
n = int(sys.stdin.readline())

number = []
for i in range(n):
    num = int(sys.stdin.readline())
    number.append(num)

number = sorted(number)

for i in number:
    print(i)