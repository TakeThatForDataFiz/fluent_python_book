def dump(**kwargs):
    return kwargs


print({"a": 0, **{"x": 1}, "y": 2, **{"z": 3, "x": 4}})

print(dump(**{"x": 1}, y=2, **{"z": 3}))
