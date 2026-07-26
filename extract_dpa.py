import fitz
doc = fitz.open(r"C:\Users\DELL\Downloads\resources\Data Protection Act.pdf")
full = []
for i, page in enumerate(doc):
    text = page.get_text()
    full.append(f"--- PAGE {i+1} ---\n{text}")
with open('dpa_full.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(full))
print(f"Done - {len(doc)} pages")
