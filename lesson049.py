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


a = Decimal('0.1')
print(a.ln())
print(a.exp())
print(a.sqrt())

import math
#print(math.ln(a))
print(math.exp(a))
print(math.sqrt(a))

print('-'*70)
x = 2
x_dec = Decimal(2)
root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()
print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(format(root_dec, '1.27f'))
print(root_dec)
print()

print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(format(root_dec * root_dec, '1.27f'))
print(root_dec * root_dec)
print()
print('-'*60)


x = 0.01
x_dec = Decimal(0.01)
print(format(x, '.27f'))
print(format(x_dec, '.27f'))
root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()
print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(format(root_dec, '1.27f'))
print(root_dec)
print()

print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(format(root_dec * root_dec, '1.27f'))
print(root_dec * root_dec)
print()
print('-'*60)

x = 0.01
x_dec = Decimal('0.01')
print(format(x, '.27f'))
print(format(x_dec, '.27f'))
root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()
print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(format(root_dec, '1.27f'))
print(root_dec)
print()

print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(format(root_dec * root_dec, '1.27f'))
print(root_dec * root_dec)
print()
print('-'*60)



