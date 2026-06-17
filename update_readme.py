import os

# ==========================================
# 1. THE CURRICULUM CONFIGURATION
# Update this dictionary when you plan out future phases!
# ==========================================
CURRICULUM = [
    {
        "pillar_title": "### 🏛️ Pillar 1: Linear Algebra (Days 1–30)",
        "phases": [
            {"title": "#### Phase 1: Vectors & The Geometry of Data (Days 1–7)", "start": 1, "end": 7},
            {"title": "#### Phase 2: Matrices & Neural Network Computations (Days 8–14)", "start": 8, "end": 14},
            {"title": "#### Phase 3: Linear Transformations & Feature Engineering (Days 15–21)", "start": 15, "end": 21},
            {"title": "#### Phase 4: Advanced AI Algebra & Decompositions (Days 22–30)", "start": 22, "end": 30},
        ]
    },
    {
        "pillar_title": "### 🏛️ Pillar 2: Multivariate Calculus (Days 31–55)",
        "phases": [
            # Example of how you will add phases on Day 31:
            # {"title": "#### Phase 1: Limits & Derivatives (Days 31–40)", "start": 31, "end": 40},
        ]
    },
    {
        "pillar_title": "### 🏛️ Pillar 3: Probability & Statistics (Days 56–85)",
        "phases": [] # Leave empty until you plan it!
    },
    {
        "pillar_title": "### 🏛️ Pillar 4: Optimization & Core ML Math (Days 86–100)",
        "phases": [] # Leave empty until you plan it!
    }
]

def update_readme():
    # 2. Scan your directory for completed days
    completed_days = {}
    for f in os.listdir('.'):
        if os.path.isdir(f) and f.startswith('Day_'):
            parts = f.split('_', 2)
            if len(parts) >= 3:
                day_num = int(parts[1])
                topic = parts[2].replace('_', ' ')
                completed_days[day_num] = f"* **Day {day_num:03d}:** [{topic}](./{f})"

    # 3. Build the Markdown lines dynamically based on the Configuration
    curriculum_lines = []
    
    for pillar in CURRICULUM:
        curriculum_lines.append(pillar["pillar_title"])
        
        if not pillar["phases"]:
            curriculum_lines.append("*(Topics will unlock when we reach this pillar...)*\n")
            continue

        for phase in pillar["phases"]:
            curriculum_lines.append(phase["title"])
            
            # Find all completed days that fall within this phase's start and end range
            days_in_phase = [
                completed_days[d] for d in sorted(completed_days.keys()) 
                if phase["start"] <= d <= phase["end"]
            ]
            
            if days_in_phase:
                curriculum_lines.extend(days_in_phase)
            else:
                curriculum_lines.append("*(No topics completed in this phase yet)*")
            
            curriculum_lines.append("") # Add a blank line for readability

    # 4. Define the static header of the README
    header = """# 100 Days of Math for AI 🧮

A personal, 100-day rigorous challenge to build the foundational mathematics of Artificial Intelligence and Machine Learning from scratch.

**The Golden Rule:** No machine learning libraries (`scikit-learn`, `PyTorch`, `TensorFlow`) are allowed. All algorithms are implemented using standard Python and `NumPy` to ensure a deep, mechanical understanding of the theory.

## ⚙️ Tech Stack
* **Language:** Python
* **Math/Arrays:** NumPy
* **Environment:** Jupyter Notebooks (VS Code)
* **Documentation:** LaTeX + Markdown

---

## 🚀 Progress Tracker

"""

    # 5. Combine and Overwrite
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(header + "\n".join(curriculum_lines))
        
    print("✅ README updated! Dynamic curriculum generated successfully.")

if __name__ == "__main__":
    update_readme()