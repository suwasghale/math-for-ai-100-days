import os

def update_readme():
    # 1. Look at your folders and build the list
    folders = sorted([f for f in os.listdir('.') if os.path.isdir(f) and f.startswith('Day_')])
    
    lines = []
    for f in folders:
        parts = f.split('_', 2)
        if len(parts) >= 3:
            day_num = int(parts[1])
            topic = parts[2].replace('_', ' ')
            lines.append(f"* **Day {day_num}:** [{topic}](./{f})")
            
    progress_text = "\n".join(lines) if lines else "*No days completed yet.*"

    # 2. Define the ENTIRE README right here in the Python file
    readme_content = f"""# 100 Days of Math for AI 🧮

A personal, 100-day rigorous challenge to build the foundational mathematics of Artificial Intelligence and Machine Learning from scratch.

**The Golden Rule:** No machine learning libraries (`scikit-learn`, `PyTorch`, `TensorFlow`) are allowed. All algorithms are implemented using standard Python and `NumPy` to ensure a deep, mechanical understanding of the theory.

## ⚙️ Tech Stack
* **Language:** Python
* **Math/Arrays:** NumPy
* **Environment:** Jupyter Notebooks (VS Code)
* **Documentation:** LaTeX + Markdown

## 🚀 Progress Tracker
{progress_text}
"""

    # 3. Obliterate the old README and write this fresh one
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
        
    print("✅ README.md generated from scratch successfully!")

if __name__ == "__main__":
    update_readme()