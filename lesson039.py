x  = 0.1
print(format(x, '.25f'))
print(x)

x  = 0.125
print(format(x, '.25f'))
print(x)

x  = 0.125 + 0.125 + 0.125
y = 0.375
print(format(x, '.25f'))
print(x)
print( x == y )
print()

x  = 0.1
print(format(x, '.25f'))
print(x)

x = 0.1 + 0.1 + 0.1
y = 0.3
print(format(x, '.25f'))
print(x)
print( x == y )
print()

print(format(x, '.25f'))
print(format(y, '.25f'))
print(round(x, 3) == round(y, 3))
print()

x = 10_000.01
y = 10_000.02
a = 0.01
b = 0.02
print(y/x)
print(b/a)
print(round(x, 1) == round(y,1))
print(round(a, 1) == round(b,1))
print('-'*50)


from math import isclose

x = 0.1 + 0.1 + 0.1
y = 0.3

print(isclose(x, y))
print(x == y)
print('='*50)

x = 123456789.01
y = 123456789.02
print(isclose(x, y, rel_tol=0.01))
print()

x = 0.01
y = 0.02
print(isclose(x, y, rel_tol=0.01))
print()

x = 0.0000001
y = 0.0000002
print(isclose(x, y, rel_tol=0.01))
print(isclose(x, y, rel_tol=0.01, abs_tol=0.01))
print()

x = 0.0000001
y = 0.0000002
a = 123456789.01
b = 123456789.02
print(isclose(x, y, rel_tol=0.0001, abs_tol=0.01))
print(isclose(a, b, rel_tol=0.0001, abs_tol=0.01))
print()





