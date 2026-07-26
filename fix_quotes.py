with open('redraft_paper.py', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

fixed = 0
for i in range(len(lines)):
    line = lines[i]
    stripped = line.strip()
    if stripped.startswith("'"):
        # Check if it ends with curly quote but no ASCII closing quote
        rstrip = line.rstrip()
        if rstrip.endswith('\u2019') and not rstrip.endswith("'"):
            # Add closing ASCII quote
            lines[i] = line + "'"
            fixed += 1

content = '\n'.join(lines)
with open('redraft_paper.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed {fixed} lines")
