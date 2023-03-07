"""Build an index mapping word -> list of occurrences"""

import collections
import re
import sys

WORD_RE = re.compile(r"\w+")

index = collections.defaultdict(list)


with open("ch3_dicts_and_sets\\this.txt", encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)

# display in abc order
for word in sorted(index, key=str.upper):
    print(word, index[word])
