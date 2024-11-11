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




