num_dec = input("Enter a number in decimal between 0-255: ")
num_bin = []
pow = 8
for x in range(8):
    pow -= 1
    if num_dec - 2 ** pow >= 0:
        num_bin.append("1")
        num_dec -= 2 ** pow
    else:
        num_bin.append("0")
print(f"'{num_dec}' in Binary is '{"".join(num_bin)}'")