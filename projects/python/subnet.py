N = int(input("How many network do you want: "))
n = 0

while 2 ** n <= N:
    n += 1
print(N)
print(f"2^{n} = {2 ** n}")
