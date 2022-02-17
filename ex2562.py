number = []

for i in range(9):
    num = int(input())
    number.append(num)

max = number[0]

for n in number:
    if n > max:
        max = n

print(max)
i = number.index(max)
print(i+1)