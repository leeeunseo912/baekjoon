import sys

input = sys.stdin.readline

n = int(input())
num = []
for i in range(n):
    number = int(input())
    if number == 0:
        num.pop()
    else:
        num.append(number)
# print(num)
sum = 0
for i in num:
    sum += i
print(sum)
