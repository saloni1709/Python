Roman = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

num = int(input("Enter a number: "))   # e.g. 3749
result = ""

while num > 0:
    for value in Roman:        # 1000, 900, 500 ...
        if num >= value:
            result += Roman[value]
            num -= value       # same process repeat
            break

print("Roman:", result)
