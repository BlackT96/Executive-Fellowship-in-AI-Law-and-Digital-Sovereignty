with open('C:\\Users\\DELL\\research\\curriculum_cleaned.txt', 'rb') as f:
    raw = f.read()
text = raw.decode('latin-1')
# Find all occurrences of "Week" and print surrounding context
import re
for m in re.finditer(r'Week \d', text):
    pos = m.start()
    snippet = text[pos:pos+120]
    # clean for output
    clean = ''.join(c if ord(c) >= 32 and ord(c) < 127 else ' ' for c in snippet)
    print(f'Pos {pos}: {clean}')
    print()
