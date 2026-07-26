import re
with open('kurose_excerpts.txt','r',encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'===== (.*?) =====', text):
    name = m.group(1)
    # Strip all non-ASCII
    clean = ''.join(c if ord(c) < 128 else ' ' for c in name)
    clean = re.sub(r'\s+', ' ', clean).strip()
    print(clean)
