import re
with open('C:\\Users\\DELL\\research\\curriculum_cleaned.txt', 'rb') as f:
    raw = f.read()
text = raw.decode('latin-1').replace('\x96', '-').replace('\x92', "'").replace('\x93', '"').replace('\x94', '"').replace('\x97', '-')
idx = text.find('Week 3')
if idx < 0:
    idx = text.find('week 3')
if idx >= 0:
    result = text[idx:idx+2000]
    with open('C:\\Users\\DELL\\research\\week3_info.txt', 'w', encoding='utf-8') as f:
        f.write(result)
    print('Written to week3_info.txt')
else:
    print('Week 3 not found')
