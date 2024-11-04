import re

# Path to the file
file_path = r"C:\Users\RC_Student_lab\Desktop\Web project\News\news.html"

# Read the file
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Find all case-insensitive occurrences of 'lorem'
matches = re.findall(r'lorem', content, re.IGNORECASE)

# Replace each occurrence with 'boo1', 'boo2', 'boo3', etc.
for i, match in enumerate(matches, start=1):
    content = re.sub(r'\blorem\b', f'boo{i}', content, 1, flags=re.IGNORECASE)

# Write the modified content back to the file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(content)

print("Replacements complete!")
