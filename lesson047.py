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
print()
print()

print(decimal.getcontext())
decimal.getcontext().prec=6

a = Decimal('0.123456789')
print(a)

decimal.getcontext().prec=2
a = Decimal('0.12345')
b = Decimal('0.12345')
print(a, b)
print(0.12345 + 0.12345)
print(a + b)

decimal.getcontext().prec=6
a = Decimal('0.12345')
b = Decimal('0.12345')
print(a, b)
print(0.12345 + 0.12345)
print(a + b)

with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print('c within local context: {0}'.format(c))

print('c within global context: {0}'.format(c))


