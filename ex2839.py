num = int(input(""))

bucket = 0

while True:
    if num % 5 == 0:
        bucket = bucket + (num//5)
        print(bucket)
        break

    num -= 3
    bucket += 1

    if num < 0:
        print("-1")
        break
