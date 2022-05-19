num = int(input())

nums = []
for i in range(num):
    [a,b] = map(int, input().split())
    nums.append([a,b])

sort_nums = sorted(nums)

for i in range(num):
    print(sort_nums[i][0], sort_nums[i][1])