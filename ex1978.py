import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))


prime = 0
# print(num_list)

for i in num_list:
    error = 0
    if i > 1:
        for j in range(2, i+1):
            if i % j == 0:
                error += 1
                # print("error" , error)
        if error == 1:
            prime += 1
    
print(prime)