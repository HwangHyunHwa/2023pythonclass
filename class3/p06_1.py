print("===1부터 n까지의 짝수의 합 구하기===")
digit=2
sum = 0
n = int(input("어디까지의 합 ? "))
while (digit<=n):
    sum = sum + digit
    digit = digit + 2
print("1부터 ", n, "까지의 합 = ", sum)
