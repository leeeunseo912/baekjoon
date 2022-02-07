n = int(input(""))

for i in range(n):
    data =  list(map(int, input().split()))
    num = data[0]
    total_score = sum(data[1:])
    avg = total_score / num
    
    cnt = 0

    for score in data[1:]:
        if score > avg:
            cnt += 1
    rate = cnt/num * 100
    print(f'{rate:.3f}%')
