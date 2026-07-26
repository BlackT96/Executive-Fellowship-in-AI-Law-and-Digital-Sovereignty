import fitz, sys, re
sys.stdout.reconfigure(encoding='utf-8')

# Kenya DPA - Section 50
doc = fitz.open(r'C:\Users\DELL\Downloads\Resources\Kenya Data-Protection-Act-1.pdf')
full = ''
for page in doc:
    full += page.get_text()

print('=== KENYA DPA ===')
print(f'Total chars: {len(full)}')

# Find S.50 - Transfer of personal data outside Kenya
m = re.search(r'(?<!\d)50\.\s', full)
if m:
    print(full[m.start():m.start()+2000])
else:
    # Search for transfer outside
    m2 = re.search(r'(?i)transfer.*outside', full)
    if m2:
        print(f'Found at pos {m2.start()}:')
        print(full[max(0,m2.start()-200):m2.start()+2000])

# Also look at Table of Contents for Section 50
toc_match = re.search(r'PART.*?Transfer.*?of.*?personal.*?data.*?outside', full, re.IGNORECASE|re.DOTALL)
if toc_match:
    print('\nTOC area:')
    print(toc_match.group()[:500])
