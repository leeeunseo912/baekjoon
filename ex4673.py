natural_number = set(range(1,10001))
none_selfnum = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    none_selfnum.add(i)

self_num = sorted(natural_number - none_selfnum)
for i in self_num:
    print(i)