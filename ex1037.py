num = int(input(""))
numbers = list(map(int, input().split()))

max_num = max(numbers)
min_num = min(numbers)

print(max_num * min_num)