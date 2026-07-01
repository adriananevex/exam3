def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"

    number = number.upper()
    decimal = 0
    for char in number:
        if char not in digits[:from_base]:
            return "ERROR"
        decimal = decimal * from_base + digits.index(char)

    if decimal == 0:
        return "0"

    result = []
    while decimal > 0:
        result.append(digits[decimal % to_base])
        decimal //= to_base

    return ''.join(reversed(result))

print(number_base_converter("1010", 2, 10))
print(number_base_converter("FF", 16, 10))
print(number_base_converter("255", 10, 16))
print(number_base_converter("123", 10, 2))
print(number_base_converter("Z", 36, 10))
print(number_base_converter("35", 10, 36))
print(number_base_converter("123", 1, 10))
print(number_base_converter("G", 16, 10))