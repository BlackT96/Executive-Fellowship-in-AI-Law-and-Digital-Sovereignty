import re

with open('redraft_paper.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace left single curly quote U+2018 and right single curly quote U+2019
# with escaped versions that won't break Python string parsing
content = content.replace('\u2018', '\u2018')
content = content.replace('\u2019', '\u2019')

# Actually, the issue is that these characters LOOK like regular quotes
# but are different Unicode codepoints that work fine in Python.
# Let me check what the actual characters are.

# Find all non-ASCII characters
for i, c in enumerate(content):
    if ord(c) > 127 and ord(c) < 256:
        if c in "'\u2018\u2019\u201c\u201d":
            ctx = content[max(0,i-10):i+10]
            print(f"Offset {i}: U+{ord(c):04X} context: {repr(ctx)}")
