import fitz, re

doc = fitz.open(r"C:\Users\DELL\Downloads\resources\_OceanofPDF.com_Computer_Networking_A_Top-Down_Approach_Global_Edition_8th_Edition_-_James_Kurose.pdf")

# Find page ranges for relevant sections by scanning for headers
full_text = ""
pages_text = []
for i, page in enumerate(doc):
    text = page.get_text()
    pages_text.append((i+1, text))

# Save chapter 1.5 (Protocol Layers) - likely pages around section 1.5
# Save chapter 2.2 (HTTP), 2.3 (FTP/SMTP), 2.4 (DNS)

output = []
capturing = False
current_section = ""

for pnum, text in pages_text:
    lines = text.split('\n')
    for line in lines:
        ls = line.strip()
        # Check for section headers
        if re.match(r'^1\.5\s', ls):
            capturing = True
            current_section = "1.5 Protocol Layers"
            output.append(f"\n\n===== SECTION 1.5: {ls} =====\n")
            continue
        elif re.match(r'^2\.2\s', ls):
            capturing = True
            current_section = "2.2 HTTP"
            output.append(f"\n\n===== SECTION 2.2: {ls} =====\n")
            continue
        elif re.match(r'^2\.3\s', ls):
            capturing = True
            current_section = "2.3 FTP/SMTP"
            output.append(f"\n\n===== SECTION 2.3: {ls} =====\n")
            continue
        elif re.match(r'^2\.4\s', ls):
            capturing = True
            current_section = "2.4 DNS"
            output.append(f"\n\n===== SECTION 2.4: {ls} =====\n")
            continue
        elif re.match(r'^2\.5\s', ls) or re.match(r'^1\.6\s', ls) or re.match(r'^Chapter\s', ls):
            capturing = False
            current_section = ""
        
        if capturing:
            output.append(line)

with open('kurose_excerpts.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print(f"Extracted {len(output)} lines")
print("Done")
