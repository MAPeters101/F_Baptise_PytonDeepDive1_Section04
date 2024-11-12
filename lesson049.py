import decimal
from decimal import Decimal

## n = d * (n//d) + (n%d)

x = 10
y = 3
print(type(x), type(y))
print(type(x//y), type(x%y))
print(x//y, x%y)
print(divmod(x, y))
print( x == y * (x//y) + (x%y))
print()

x = Decimal(10)
y = Decimal(3)
print(type(x), type(y))
print(type(x//y), type(x%y))
print(x//y, x%y)
print(divmod(x, y))
print( x == y * (x//y) + (x%y))
print()

x = -10
y = 3
print(type(x), type(y))
print(type(x//y), type(x%y))
print(x//y, x%y)
print(divmod(x, y))
print( x == y * (x//y) + (x%y))
print()

x = Decimal(-10)
y = Decimal(3)
print(type(x), type(y))
print(type(x//y), type(x%y))
print(x//y, x%y)
print(divmod(x, y))
print( x == y * (x//y) + (x%y))
print()
print('='*70)







