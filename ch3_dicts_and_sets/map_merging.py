d1 = {"a": 1, "b": 3}
d2 = {"a": 2, "b": 4, "c": 6}
d3 = {"a": 3, "e": 4, "f": 6}

merged = d1 | d2 | d3
print(f"{merged=}")
print(f"{d1=}")
d1 |= d2
print(f"{d1=}")
print(merged == d1)
