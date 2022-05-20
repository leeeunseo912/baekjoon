# def search(sanggeun, nums):

#     for i in range(len(nums)):
#         if nums[i] in sanggeun:
#             nums[i] = 1
#         else:
#             nums[i] = 0

#     for i in nums:
#         print(i, end=' ')

def binary_search(num):
    l = 0
    r = n -1
    while l <= r:
        mid = (l + r)//2
        if sanggeun[mid] == num:
            return 1
        elif sanggeun[mid] > num:
            r = mid -1
        else:
            l = mid + 1
    return 0

n = int(input())
sanggeun = list(map(int,input().split()))

m = int(input())
nums = list(map(int,input().split()))
sanggeun.sort()

for i in nums:
    print(binary_search(i), end = ' ')