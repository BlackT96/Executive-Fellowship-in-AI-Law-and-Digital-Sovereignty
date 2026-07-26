import fitz, os, re

res_dir = r'C:\Users\DELL\Downloads\Resources'
out_dir = r'C:\Users\DELL\research'

files = [
    'UCC Content-Regulations-2019.pdf',
    'UCC Consumer-Protection Regulations 2019.pdf',
    'UCC CERT (Computer Emergency Response Team)-Regulations-2019.pdf',
    'UCC Quality-of-Service-Regulations-2019.pdf',
    'UCC Licensing-Regulations-2019.pdf',
    'UCC Equipement-Type-Approval- Reulations 2019.pdf',
    'UCC Text-and-Multimedia-Messaging-Reulations 2019.pdf',
    'UCC Film-Documentaries-and-Commercial-Still-Photography-2019.pdf',
    'UCC Intelligent-Network-Monitoring-System- REgulations 2019.pdf',
    'UCC Centralised Equipment Identification Register -Regulations 2019.pdf',
    'UCC Fees-and-fines-Regulations-2019.pdf',
    'UCC Competition-and-Accounting-Regulations-2019.pdf',
    'UCC Pricing-and-Accounting-Regulations-2019.pdf',
    'UCC Emergency-Response-2019.pdf',
    'UCC Interconnection-Access-Copy.pdf',
    'UCC Universal-Service- Regulations 2019.pdf',
    'ucc Universal-Services-and-Access-Fund- Regulations 2019.pdf',
    'UCC Fees-and-Fines-Amendment-Regulations-2020.pdf',
    'UCC Fees-and-Fines-(Amendment)-no.2-Regulations-2020.pdf',
]

for fname in files:
    full_path = os.path.join(res_dir, fname)
    try:
        doc = fitz.open(full_path)
        text = ''
        for page in doc:
            text += page.get_text('text')
            if len(text) > 1000:
                break
        doc.close()
        
        # Clean encoding
        clean = text.encode('utf-8', errors='replace').decode('utf-8')
        
        # Find the short title / application clause
        outname = fname.replace('.pdf', '.txt')
        outpath = os.path.join(out_dir, outname)
        with open(outpath, 'w', encoding='utf-8') as f:
            f.write(clean[:1500])
        
        # Determine if internet-relevant
        lower = clean.lower()
        keywords = ['internet', 'electronic communication', 'data', 'online', 'ott', 'broadband', 'cyber', 'network service', 'information society']
        relevant = any(k in lower for k in keywords)
        
        # Find citation/short title
        title_match = re.search(r'These Regulations may be cited as[^.]+\.', clean)
        purpose_match = re.search(r'(Purpose|Application|Scope|Objective)[^.]{0,200}\.', clean, re.IGNORECASE)
        
        title = title_match.group() if title_match else '[No title found]'
        purpose = purpose_match.group() if purpose_match else '[No purpose clause found]'
        
        print(f'{fname}')
        print(f'  Title: {title[:120]}')
        print(f'  Purpose: {purpose[:200]}')
        print(f'  Internet-relevant: {relevant}')
        print()
    except Exception as e:
        print(f'{fname}: Error - {e}')
