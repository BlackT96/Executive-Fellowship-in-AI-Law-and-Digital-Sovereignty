import fitz, sys, re
sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r'C:\Users\DELL\research\Week 4 - APIs, Cloud Computing & SDLC.docx')
full = ''
for p in doc:
    full += p.get_text()

checks = [
    ('DPA Section 19', True, 'Cross-border transfer reference fixed'),
    ('DPPA Section 26', False, 'Old wrong reference removed'),
    ('ETA Section 7', True, 'Originality of electronic records fixed'),
    ('ETA Section 6', False, 'Old S.6 reference removed from SDLC section'),
    ('S.34', True, 'Court jurisdiction row added to Quick Reference'),
    ('Evidence Act + ETA S.7 requirement', True, 'Foundation-to-Tune table fixed'),
    ('Applies to acts inside or outside Uganda', True, 'S.33 practical description fixed'),
    ('Magistrate Grade 1/Chief Magistrate', True, 'S.34 description added'),
]

all_ok = True
for text, should_exist, desc in checks:
    found = text in full
    if should_exist and not found:
        print(f'FAIL: "{text}" should exist but was NOT found - {desc}')
        all_ok = False
    elif not should_exist and found:
        print(f'FAIL: "{text}" should NOT exist but WAS found - {desc}')
        all_ok = False
    else:
        status = 'OK' if should_exist else 'OK (removed)'
        print(f'{status}: {text}')

# Also print the last page to check footer
lines = full.split('\n')
for line in lines[-15:]:
    if line.strip():
        print(f'Footer: {line.strip()}')

print(f'\nAll checks passed: {all_ok}')
