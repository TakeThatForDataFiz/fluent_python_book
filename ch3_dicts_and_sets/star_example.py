food = dict(category='ice cream', flavor='vanilla', cost=159)
match food:
    case {'category': 'ice cream', **details}:
        print(f"Ice Cream Details: {details}")
    