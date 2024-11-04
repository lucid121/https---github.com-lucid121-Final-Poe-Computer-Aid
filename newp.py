import re

# Path to the HTML file
file_path = r"C:\Users\RC_Student_lab\Desktop\Web project\News\test.html"

# Read the contents of the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Counter for new file names (newp1, newp2, ...)
counter = 1

# Function to replace src attributes
def replace_src(match):
    global counter
    img_path = match.group(1)
    # Skip replacement if the file is 'user.jpg'
    if img_path == "user.jpg":
        return f'src="img/{img_path}"'
    else:
        # Generate new image name
        new_img_name = f"newp{counter}.jpg"
        counter += 1
        return f'src="img/{new_img_name}"'

# Replace src attributes, excluding 'user.jpg'
new_content = re.sub(r'src="img/(.*?)\.jpg"', replace_src, html_content)

# Write the modified content back to the HTML file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(new_content)

print("HTML file updated successfully.")
