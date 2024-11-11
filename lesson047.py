import decimal
from decimal import Decimal

print(Decimal(10))
a = Decimal(10)
print(a, type(a))

a = Decimal(-10)
print(a, type(a))

a = Decimal('10.1')
print(a, type(a))

a = Decimal('-3.1415')
print(a, type(a))

t = (0, (3,1,4,1,5), -4)
a = Decimal(t)
print(a, type(a))

a = Decimal((0, (3,1,4,1,5), -4))
print(a, type(a))

# a = Decimal(0, (3,1,4,1,5), -4)
# print(a, type(a))

a = Decimal((1, (3,1,4,1,5), -3))
print(a, type(a))

print(format(0.1, '.25f'))
print(Decimal(0.1))
print(Decimal(0.1) == Decimal('0.1'))
print(Decimal(10) == Decimal('10'))
