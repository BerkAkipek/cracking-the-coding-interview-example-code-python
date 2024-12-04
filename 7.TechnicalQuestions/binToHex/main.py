# Write a function that checks a binary number(passed as a string), equals to hexadecimal representation of the string.

def convert_from_base(base, num):
    if base < 2 or (base > 10 and base != 16):
        return -1
    val = 0
    for i in range(len(num) - 1, 0, -1):
        digit = num[i]
        if digit < 0 or digit >= base:
            return -1
        exponent = len(num) - 1 - i
        val += digit * pow(base=base, exp=exponent)
    return val


def compare_bin_to_hex(binary, hexadecimal):
    n1 = convert_from_base(base=2, num=binary)
    n2 = convert_from_base(base=16, num=hexadecimal)
    if n1 < 0 or n2 < 0:
        return False
    return n1 == n2
