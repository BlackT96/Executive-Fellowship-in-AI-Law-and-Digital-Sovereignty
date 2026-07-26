import re
with open('C:\\Users\\DELL\\research\\curriculum_cleaned.txt', 'rb') as f:
    raw = f.read()
text = raw.decode('latin-1')
idx = text.find('Week 2')
if idx < 0:
    idx = text.find('week 2')
if idx >= 0:
    snippet = text[max(0,idx-500):idx+3000]
    snippet = snippet.replace('\x96', '-').replace('\x92', "'").replace('\x93', '"').replace('\x94', '"')
    print(snippet)
else:
    print("Week 2 not found")
