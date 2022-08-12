import sys

input = sys.stdin.readline

while(True):
    triangle = list(map(int, input().split(' ')))
    triangle.sort()

    if set(triangle) == {0}:
        break
    elif (triangle[2]**2 == triangle[0]**2 + triangle[1]**2):
        print("right")
    else:
        print("wrong")