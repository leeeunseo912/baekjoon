nums = []
mods = []
for i in range(10):
    num = int(input())
    nums.append(num)
    mod = nums[i] % 42
    mods.append(mod)

count = set(mods)
print(len(count))