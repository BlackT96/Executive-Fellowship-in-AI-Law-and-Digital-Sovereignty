import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r'C:\Users\DELL\research\Week 4 - APIs, Cloud Computing & SDLC.docx')
full = ''.join(p.get_text() for p in doc)
checks = [
    'PART 5: COMPARATIVE INTERNATIONAL LEGAL FRAMEWORKS',
    'United States', 'United Kingdom', 'European Union',
    'South Africa', 'Kenya', 'Singapore',
    'AI Governance', 'CDA S.230', 'EU AI Act',
    'POPIA S.72', 'AI Bill 2026', 'Singapore',
    'API / Intermediary Liability',
    'Cloud / Data Localisation',
    'Data Protection / Security Measures',
    'SDLC / Software Liability',
]
for c in checks:
    status = 'OK' if c in full else 'MISSING'
    print(f'{status}: {c}')
print(f'\nTotal chars: {len(full)}')
