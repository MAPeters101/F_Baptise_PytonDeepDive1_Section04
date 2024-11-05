print(type(10))
#help(int)

a = int()
print(a)

a = int(10.5)
print(a)


a = int(10.999999)
print(a)

a = int(True)
print(a)

a = int(False)
print(a)

import fractions

a = fractions.Fraction(22/7)
print(type(a))
print(a)
print(float(a))
print(int(a))
print()

print(int("12345"))
print(int("101", 2))
print(int("FF", 16))
print(int("ff", 16))
print(int("8", 11))
print(int("A", 11))
#print(int("B", 11))

print('+'*10)
print(bin(10))
print(bin(5))
print(oct(10))
print(hex(255))

a = int('101', 2)
b = 0b101
print(a, b)

def from_base10(n, b):
    if b < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError("Number n must be >= 0")
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        #m, n = n % b, n // b
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits

print(from_base10(10, 2))
print(from_base10(255, 16))

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode the digits.")
    # encoding = ''
    # for d in digits:
    #     encoding += digit_map[d]
    # return encoding
    return ''.join([digit_map[d] for d in digits])


print(encode([15, 15], '0123456789ABCDEF'))

