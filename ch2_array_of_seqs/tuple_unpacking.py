t = (20, 8)

quotient, remainder = divmod(*t)
# print(quotient, remainder)


import os

_, filename = os.path.split('users/johnl/Documents/tuple_unpacking.py')
# print(filename)

a, b, *rest = range(5)
print(a)
print(b)
print(rest)