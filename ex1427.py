import sys
input = sys.stdin.readline

num = int(input())
num_list = []
for i in str(num):
    num_list.append(i)
# print(num_list)
num_list.sort()
num_list.reverse()
# print(num_list)

for i in num_list:
    print(i,end='')