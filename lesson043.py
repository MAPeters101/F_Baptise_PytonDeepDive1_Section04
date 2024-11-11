a = round(1.9)
print(a, type(a))

a = round(1.9, 0)
print(a, type(a))

print(round(1.8888, 3), round(1.8888, 2), round(1.8888, 1), round(1.8888, 0))

print(round(888.88, 1), round(888.88, 0), round(888.88, -1), round(888.88, -2), round(888.88, -3), round(888.88, -4))

print(round(9800, -4))
print(round(1.25, 1))
print(round(1.35, 1))
print()

print(round(-1.25, 1))
print(round(-1.35, 1))
print()

# def round(x):
#     return 'a'

print(round(10.5))

def _round(x):
    from math import copysign
    return int(x + 0.5 * copysign(1, x))

print(round(1.5), _round(1.5))
print(round(2.5), _round(2.5))

print(round(-1.5), _round(-1.5))
print(round(-2.5), _round(-2.5))




