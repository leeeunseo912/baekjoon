num = int(input(""))
nums = []
for i in range(num):
    n = int(input(""))
    nums.append(n) 

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
for i in nums:
    print(i)