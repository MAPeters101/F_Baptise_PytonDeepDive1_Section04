import decimal
from decimal import Decimal

print(decimal.getcontext())
print(decimal.getcontext().prec)
print(decimal.getcontext().rounding)
print()

decimal.getcontext().prec = 6
print(decimal.getcontext())
print(decimal.getcontext().prec)

g_ctx = decimal.getcontext()
print(type(g_ctx))

print(decimal.getcontext().rounding)
g_ctx.rounding = 'ROUND_HALF_UP'
print(decimal.getcontext().rounding)
g_ctx.rounding = decimal.ROUND_HALF_UP
print(decimal.getcontext().rounding)
print(type(decimal.ROUND_HALF_UP))
print(decimal.ROUND_HALF_UP)

g_ctx.prec = 28
g_ctx.rounding = decimal.ROUND_HALF_EVEN
print(decimal.getcontext())
print()

print(decimal.localcontext())
print(type(decimal.localcontext()))
print(type(decimal.getcontext()))
print()

x = Decimal('1.25')
y = Decimal('1.35')

with decimal.localcontext() as ctx:
    print(type(ctx))
    print(ctx)
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print(ctx)
    print(decimal.getcontext())
    print(id(ctx))
    print(id(decimal.getcontext()))
    print(id(ctx) == id(decimal.getcontext()))
    print(round(x, 1))
    print(round(y, 1))


print('-+'*30)
print(decimal.getcontext())
print(id(decimal.getcontext()))
print(round(x, 1))
print(round(y, 1))



