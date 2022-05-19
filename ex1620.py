import sys

input =sys.stdin.readline
dic, num = map(int,input().split())

dic_list = {}

for i in range(1, dic+1):
    word = input().rstrip()
    dic_list[i] = word
    dic_list[word] = i

for i in range(num):
    find = input().rstrip()
    if find.isdigit():
        print(dic_list[int(find)])
    else:
        print(dic_list[find])
