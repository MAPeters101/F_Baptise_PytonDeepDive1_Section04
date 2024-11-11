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
print()


