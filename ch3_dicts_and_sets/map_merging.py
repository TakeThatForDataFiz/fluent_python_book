d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c':6}

merged = d1 | d2 
d1 |= d2
print(merged == d1)