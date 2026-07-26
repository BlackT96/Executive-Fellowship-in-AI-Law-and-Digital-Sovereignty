import fitz, sys, re
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r'C:\Users\DELL\Downloads\Resources\Kenya Data-Protection-Act-1.pdf')
full = ''
for page in doc:
    full += page.get_text()

# Find the actual full text of Section 50
# The TOC shows it's "Processing through a data server or data centre in Kenya"
# Search for the actual section content (not in TOC)
idx = full.find('Processing through a data server or data centre in Kenya')
if idx >= 0:
    print('Found at pos', idx)
    # Get the content after the heading
    print(full[idx:idx+3000])
else:
    print('Not found by heading, searching by section marker')
    m = re.search(r'(?<!\d)50\.\s+[Pp]rocessing', full)
    if m:
        print(full[m.start():m.start()+2500])

# Also get Section 26 - Transfer of personal data outside Kenya
print('\n\n=== SECTION 26 ===')
m26 = re.search(r'(?<!\d)26\.\s', full)
if m26:
    print(full[m26.start():m26.start()+2500])
