import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))

error = 0
prime = 0
print(num_list)

for i in num_list:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
                print("error" , error)
        if error == 0:
            prime += 1
    
print(prime)