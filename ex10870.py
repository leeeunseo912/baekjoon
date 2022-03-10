def Fibo(num):
    if num == 0:
        return 0
    elif num == 1 or num ==2:
        return 1
    else:
        return Fibo(num-1) + Fibo(num-2)

num = int(input(""))

print(Fibo(num))