from fractions import Fraction

#help(Fraction)

print(Fraction(1))
print(Fraction(denominator=1, numerator=2))
print(Fraction(2, 1))
print(Fraction(1, 2))
print(Fraction(numerator=2, denominator=1))
print(Fraction(0.125))
print(Fraction('0.125'))
print(Fraction('22/7'))
print('='*10)
x = Fraction(2, 3)
y = Fraction(3, 4)
print(x + y)
print(x * y)
print(x / y)
print(Fraction(8, 16))
print(Fraction(1, -4))
x = Fraction(1, -4)
print(x.numerator)
print(x.denominator)
print('-'*10)

import math
x = Fraction(math.pi)
print(x)
print(float(x))

y = Fraction(math.sqrt(2))
print(y)
print(float(y))
print()

a = 0.125
print(a)
b = 0.3
print(b)
print(Fraction(a))
print(Fraction(b))
print(format(b, '0.5f'))
print(format(b, '0.15f'))
print(format(b, '0.25f'))
print()

x = Fraction(0.3)
print(x.limit_denominator(10))

x = Fraction(math.pi)
print(x)
print(float(x))
print(x.limit_denominator(10))
print(22/7)
print(x.limit_denominator(100))
print(x.limit_denominator(100_000))
print(312689/99532)

