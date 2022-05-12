import time
import sys
# start = time.time()
num = int(sys.stdin.readline())
nums = []
for i in range(num):
    nums.append(int(sys.stdin.readline()))

for i in sorted(nums):
    print(i)

# print("time : ", time.time() -start)