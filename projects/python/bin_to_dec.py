num_bin = input("Enter a number in Binary in 8 digits: ")
num_dec = 0
pow = 8
for digit in num_bin:
    pow -= 1
    if digit == "0":
        continue
    else:
        num_dec += 2 ** pow
print(f"'{num_bin}' in Decimal is '{num_dec}'")