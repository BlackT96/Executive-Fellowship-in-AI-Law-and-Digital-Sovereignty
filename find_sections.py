with open('kurose_excerpts.txt','r',encoding='utf-8') as f:
    text = f.read()

import re
targets = [
    'SECTION 1.5: 1.5 Protocol Layers',
    'SECTION 2.2: 2.2 The Web and HTTP',
    'SECTION 2.4: 2.4 DNS'
]
for t in targets:
    idx = text.find(t)
    if idx >= 0:
        # Get surrounding context
        start = max(0, idx - 50)
        end = min(len(text), idx + len(t) + 50)
        print(f'Found at offset {idx}: ...{repr(text[start:end])}...')
