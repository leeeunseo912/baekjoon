fixed_cost, cost, price = map(int, input().split())

if cost >= price:
    print(-1)

else:
    print(fixed_cost//(price-cost)+1)