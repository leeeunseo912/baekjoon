num = int(input())

for i in range(num):
    test = list(input())
    score = 0
    total_score = 0
    for i in test:
        if i == 'O':
            score += 1
            total_score += score
        else: 
            score = 0

    print(total_score)