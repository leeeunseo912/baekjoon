num = int(input())
line = 0
max = 0

while num > max:
    line += 1
    max += line

gap = max - num

if line % 2 == 0:
    a = line - gap
    b = gap + 1
else:
    a = gap + 1
    b = line - gap

print(f'{a}/{b}')
