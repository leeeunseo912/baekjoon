n, new_score, p = map(int, input().split())

if n:
    scores = list(map(int,input().split()))
    scores.append(new_score)
    scores.sort(reverse=True)
    rank = scores.index(new_score) + 1

    if rank > p:
        print(-1)
    else:
        if n == p and new_score == scores[-1]:
            print(-1)
        else:
            print(rank)

else:
    print(1)