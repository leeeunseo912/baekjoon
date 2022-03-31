bug1 = int(input(""))
bug2 = int(input(""))
bug3 = int(input(""))
coke =  int(input(""))
cider =  int(input(""))


result1 = bug1 + min(coke, cider) - 50
result2 = bug2 + min(coke, cider) - 50
result3 = bug3 + min(coke, cider) - 50

print(min(result1, result2, result3))