"""Build an Index mapping word -> list of occurrences"""
import re
import sys


WORD_RE = re.compile(r"\w+")

index = {}
# use zen python object instead of cmd line sys.argv[1]
with open("ch3_dicts_and_sets\\this.txt", encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # coded ugly on purpose
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

# display in abc order
for word in sorted(index, key=str.upper):
    print(word, index[word])
