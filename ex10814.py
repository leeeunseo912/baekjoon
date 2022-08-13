import sys

input = sys.stdin.readline

n = int(input())

members = [[0 for x in range(2)] for y in range(n)]
for i in range(n):
    age, name = input().split(' ')
    members[i][0] = int(age)
    members[i][1] = name

members.sort(key = lambda x:x[0])
# print(members)
for i in range(n):
    print(members[i][0], members[i][1].strip())
 
