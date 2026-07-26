import fitz, os

res_dir = r'C:\Users\DELL\Downloads\Resources'
files_to_check = [
    'UCC Content-Regulations-2019.pdf',
    'UCC Consumer-Protection Regulations 2019.pdf',
    'UCC Quality-of-Service-Regulations-2019.pdf',
    'UCC CERT (Computer Emergency Response Team)-Regulations-2019.pdf',
    'UCC Equipement-Type-Approval- Reulations 2019.pdf',
    'UCC Text-and-Multimedia-Messaging-Reulations 2019.pdf',
    'UCC Film-Documentaries-and-Commercial-Still-Photography-2019.pdf',
    'UCC Intelligent-Network-Monitoring-System- REgulations 2019.pdf',
    'UCC Centralised Equipment Identification Register -Regulations 2019.pdf',
    'UCC Licensing-Regulations-2019.pdf',
]

for fname in files_to_check:
    full_path = os.path.join(res_dir, fname)
    if os.path.exists(full_path):
        doc = fitz.open(full_path)
        text = ''
        for i, page in enumerate(doc):
            text += page.get_text()
            if i < 2:  # First 2 pages
                pass
        doc.close()
        # Save to temp file for reading
        outname = fname.replace('.pdf', '.txt').replace(' ', '_')
        outpath = os.path.join(r'C:\Users\DELL\research', outname)
        with open(outpath, 'w', encoding='utf-8') as f:
            f.write(text[:2000])
        print(f'{fname} -> saved')
