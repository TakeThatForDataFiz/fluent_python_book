# generate list without list comprehension
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

# print(codes)


# use a list comprehension
codes = [ord(symbol) for symbol in symbols]
print(codes)
