num = int(input(""))

scores=[]
scores = list(map(int, input().split()))

high_score = max(scores)

new_scores = []
for i in range(num):
    new_score = scores[i] / high_score * 100
    new_scores.append(new_score)

total = 0
for i in new_scores:
    total += i

result = total/num
print(result)