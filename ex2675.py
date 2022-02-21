num = int(input(""))

for i in range(num):
    R, S = input().split()
    for j in S:
        print(int(R) * j, end="")
    print()