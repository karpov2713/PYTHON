from pizza import make_pizza as mp
import math

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

print('  π: {:.30f}'.format(math.pi))
print('  e: {:.30f}'.format(math.e))
print('nan: {:.30f}'.format(math.nan))
print('inf: {:.30f}'.format(math.inf))