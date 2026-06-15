import os
import re

def update_readme():
    readme_path = 'README.md'
    
    # 1. Find all Day_ folders and sort them
    folders = [f for f in os.listdir('.') if os.path.isdir(f) and f.startswith('Day_')]
    folders.sort()
    
    # 2. Generate the markdown links
    progress_lines = []
    for folder in folders:
        # Extract "001" and "Vectors_and_Tensors" from "Day_001_Vectors_and_Tensors"
        parts = folder.split('_', 2)
        if len(parts) >= 3:
            day_num = int(parts[1])
            topic = parts[2].replace('_', ' ')
            progress_lines.append(f"* **Day {day_num}:** [{topic}](./{folder})")
            
    if not progress_lines:
        progress_text = "*No days completed yet. Starting soon!*\n"
    else:
        progress_text = "\n".join(progress_lines) + "\n"

    # 3. Read the current README
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 4. Replace the content between the tags
    start_tag = "\n"
    end_tag = ""
    
    pattern = re.compile(f"({start_tag}).*?({end_tag})", re.DOTALL)
    new_content = pattern.sub(rf"\1{progress_text}\2", content)

    # 5. Write the updated content back
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("✅ README.md successfully updated!")

if __name__ == "__main__":
    update_readme()